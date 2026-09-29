"""Save and restore local projects in Google Drive's VibeProjects folder."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import sys
import tempfile
import zipfile

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


CONFIG = Path.home() / ".vibe-drive"
CREDENTIALS = CONFIG / "credentials.json"
TOKEN = CONFIG / "token.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]
FOLDER_NAME = "VibeProjects"
FOLDER_MIME = "application/vnd.google-apps.folder"
EXCLUDE_DIRS = {
    ".git", ".venv", "venv", "node_modules", ".next", ".gradle",
    "__pycache__", ".cache", "tmp", "temp",
}
EXCLUDE_FILES = (
    ".env", ".env.*", "credentials.json", "token.json", "*.pem",
    "*.key", "*.p12", "*.pfx", "*.keystore", "*.mobileprovision",
    "client_secret*.json", "*apps.googleusercontent.com.json", ".npmrc",
    "id_rsa", "id_ed25519", "secrets.json",
)


class VibeDriveError(Exception):
    pass


def save_token(credentials: Credentials) -> None:
    CONFIG.mkdir(mode=0o700, parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=CONFIG,
                                     prefix=".token-", delete=False) as handle:
        temp_path = Path(handle.name)
        handle.write(credentials.to_json())
    try:
        if os.name != "nt":
            temp_path.chmod(0o600)
        temp_path.replace(TOKEN)
    finally:
        temp_path.unlink(missing_ok=True)


def authorize() -> Credentials:
    if not CREDENTIALS.is_file():
        raise VibeDriveError(f"OAuth client file missing: {CREDENTIALS}. Run the installer first.")
    flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS), SCOPES)
    credentials = flow.run_local_server(port=0, prompt="consent")
    save_token(credentials)
    return credentials


def drive_service():
    if not TOKEN.is_file():
        raise VibeDriveError("No saved token. Run the 'auth' command first.")
    credentials = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not credentials.valid:
        if not credentials.refresh_token:
            raise VibeDriveError("Token has no refresh token. Run the 'auth' command again.")
        try:
            credentials.refresh(Request())
        except RefreshError as error:
            raise VibeDriveError("Google authorization expired. Run the 'auth' command again.") from error
        save_token(credentials)
    return build("drive", "v3", credentials=credentials, cache_discovery=False)


def quote_query(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "\\'")


def find_files(service, query: str, fields: str) -> list[dict]:
    files = []
    page_token = None
    while True:
        result = service.files().list(
            q=query, spaces="drive", fields=f"nextPageToken,files({fields})",
            pageSize=1000, pageToken=page_token,
        ).execute()
        files.extend(result.get("files", []))
        page_token = result.get("nextPageToken")
        if not page_token:
            return files


def folder_id(service, create: bool) -> str:
    query = (f"name = '{quote_query(FOLDER_NAME)}' and mimeType = '{FOLDER_MIME}' "
             "and 'root' in parents and trashed = false")
    folders = find_files(service, query, "id,name")
    if len(folders) > 1:
        raise VibeDriveError(f"Multiple {FOLDER_NAME} folders exist at Drive root; resolve the duplicate first.")
    if folders:
        return folders[0]["id"]
    if not create:
        raise VibeDriveError(f"Drive folder {FOLDER_NAME} was not found.")
    folder = service.files().create(
        body={"name": FOLDER_NAME, "mimeType": FOLDER_MIME, "parents": ["root"]},
        fields="id",
    ).execute()
    return folder["id"]


def zip_files(service, parent_id: str, name: str | None = None) -> list[dict]:
    query = f"'{quote_query(parent_id)}' in parents and trashed = false"
    if name is not None:
        query += f" and name = '{quote_query(name)}'"
    return find_files(service, query, "id,name,size,md5Checksum,mimeType")


def valid_project_name(name: str) -> str:
    if not name or name in {".", ".."} or "/" in name or "\\" in name:
        raise VibeDriveError("Project name must be a single folder name.")
    return name


def omit_file(name: str) -> bool:
    lower = name.lower()
    return any(fnmatch.fnmatchcase(lower, pattern) for pattern in EXCLUDE_FILES)


def make_zip(project: Path, destination: Path) -> tuple[int, int]:
    included = excluded = 0
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=6, allowZip64=True) as archive:
        for current, dirs, files in os.walk(project, followlinks=False):
            root = Path(current)
            kept_dirs = []
            for dirname in dirs:
                path = root / dirname
                if dirname in EXCLUDE_DIRS or path.is_symlink():
                    excluded += 1
                else:
                    kept_dirs.append(dirname)
            dirs[:] = kept_dirs
            for filename in files:
                path = root / filename
                if omit_file(filename) or path.is_symlink() or not path.is_file():
                    excluded += 1
                    continue
                archive.write(path, path.relative_to(project).as_posix())
                included += 1
    if not included:
        raise VibeDriveError("No project files remain after exclusions; nothing was uploaded.")
    return included, excluded


def md5_file(path: Path) -> str:
    digest = hashlib.md5()  # Google Drive supplies MD5 for binary files.
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_upload(request):
    response = None
    while response is None:
        _, response = request.next_chunk()
    return response


def save_project(service, raw_project: str) -> None:
    project = Path(raw_project).expanduser().resolve()
    if not project.is_dir():
        raise VibeDriveError(f"Project folder not found: {project}")
    if project in {Path.home().resolve(), Path(project.anchor)}:
        raise VibeDriveError("Choose a project folder, not your home or filesystem root.")
    name = valid_project_name(project.name)
    with tempfile.TemporaryDirectory(prefix="vibe-drive-save-") as temporary:
        archive_path = Path(temporary) / f"{name}.zip"
        included, excluded = make_zip(project, archive_path)
        parent_id = folder_id(service, create=True)
        matches = zip_files(service, parent_id, archive_path.name)
        if len(matches) > 1:
            raise VibeDriveError(f"Multiple {archive_path.name} files exist in {FOLDER_NAME}; resolve the duplicate first.")
        media = MediaFileUpload(str(archive_path), mimetype="application/zip",
                                resumable=True, chunksize=8 * 1024 * 1024)
        if matches:
            request = service.files().update(fileId=matches[0]["id"], media_body=media,
                                              fields="id,name,size,md5Checksum,parents")
        else:
            request = service.files().create(
                body={"name": archive_path.name, "mimeType": "application/zip", "parents": [parent_id]},
                media_body=media, fields="id,name,size,md5Checksum,parents",
            )
        uploaded = run_upload(request)
        verified = service.files().get(
            fileId=uploaded["id"], fields="id,name,size,md5Checksum,parents,trashed"
        ).execute()
        expected_md5 = md5_file(archive_path)
        if (verified.get("name") != archive_path.name or verified.get("trashed")
                or parent_id not in verified.get("parents", [])
                or int(verified.get("size", -1)) != archive_path.stat().st_size
                or verified.get("md5Checksum") != expected_md5):
            raise VibeDriveError("Upload returned, but Drive verification did not match the local ZIP.")
        print(f"Saved {archive_path.name} to Drive/{FOLDER_NAME} ({included} files; {excluded} omitted).")


def list_projects(service) -> None:
    try:
        parent_id = folder_id(service, create=False)
    except VibeDriveError as error:
        if "was not found" in str(error):
            print("No saved projects yet.")
            return
        raise
    files = sorted((item for item in zip_files(service, parent_id)
                    if item["name"].lower().endswith(".zip")), key=lambda item: item["name"].lower())
    if not files:
        print("No saved projects yet.")
    for item in files:
        print(f"{item['name']}\t{item.get('size', '?')} bytes")


def safe_extract(archive_path: Path, staging: Path) -> int:
    count = 0
    with zipfile.ZipFile(archive_path) as archive:
        for entry in archive.infolist():
            name = entry.filename
            path = PurePosixPath(name)
            mode = (entry.external_attr >> 16) & 0o170000
            if (not name or name.startswith("/") or "\\" in name or
                    (path.parts and ":" in path.parts[0]) or
                    path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts) or
                    mode == stat.S_IFLNK):
                raise VibeDriveError(f"Unsafe ZIP entry: {name!r}")
            target = staging.joinpath(*path.parts)
            if entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(entry) as source, target.open("xb") as output:
                shutil.copyfileobj(source, output)
            count += 1
    return count


def restore_project(service, raw_name: str, raw_target: str | None) -> None:
    name = valid_project_name(raw_name.removesuffix(".zip"))
    target = (Path(raw_target).expanduser() if raw_target else Path.cwd() / name).absolute()
    if target.exists() or target.is_symlink():
        raise VibeDriveError(f"Destination already exists; refusing to overwrite: {target}")
    parent_id = folder_id(service, create=False)
    matches = zip_files(service, parent_id, f"{name}.zip")
    if not matches:
        raise VibeDriveError(f"{name}.zip was not found in Drive/{FOLDER_NAME}.")
    if len(matches) > 1:
        raise VibeDriveError(f"Multiple {name}.zip files exist; resolve the duplicate first.")
    source = matches[0]
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".vibe-drive-restore-", dir=target.parent) as temporary:
        temporary_path = Path(temporary)
        archive_path = temporary_path / f"{name}.zip"
        with archive_path.open("wb") as output:
            request = service.files().get_media(fileId=source["id"])
            downloader = MediaIoBaseDownload(output, request, chunksize=8 * 1024 * 1024)
            complete = False
            while not complete:
                _, complete = downloader.next_chunk()
        if source.get("md5Checksum") and md5_file(archive_path) != source["md5Checksum"]:
            raise VibeDriveError("Downloaded ZIP checksum does not match Drive metadata.")
        staging = temporary_path / "project"
        staging.mkdir()
        count = safe_extract(archive_path, staging)
        if target.exists() or target.is_symlink():
            raise VibeDriveError(f"Destination appeared during restore: {target}")
        staging.rename(target)
    print(f"Restored {name} to {target} ({count} files).")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    save_cmd = commands.add_parser("save", help="Save a project folder as a ZIP in Drive")
    save_cmd.add_argument("project", nargs="?", default=".")
    commands.add_parser("list", help="List saved project ZIP files")
    restore_cmd = commands.add_parser("restore", help="Restore a project into a new folder")
    restore_cmd.add_argument("name")
    restore_cmd.add_argument("--to", dest="target")
    commands.add_parser("auth", help="Authorize Drive access in a browser")
    args = parser.parse_args()
    try:
        if args.command == "auth":
            authorize()
            print(f"Google Drive authorization saved at {TOKEN}")
            return 0
        service = drive_service()
        if args.command == "save":
            save_project(service, args.project)
        elif args.command == "list":
            list_projects(service)
        else:
            restore_project(service, args.name, args.target)
    except VibeDriveError as error:
        print(f"Vibe Drive: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

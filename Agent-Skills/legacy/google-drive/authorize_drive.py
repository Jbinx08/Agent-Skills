"""Authorize this local project to access Google Drive and save token.json."""

from pathlib import Path
import json
import sys

from google_auth_oauthlib.flow import InstalledAppFlow


BASE_DIR = Path(__file__).resolve().parent
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
TOKEN_FILE = BASE_DIR / "token.json"

# Allows this app to list, upload, download, and update files in Drive.
SCOPES = ["https://www.googleapis.com/auth/drive"]


def main() -> int:
    if not CREDENTIALS_FILE.exists():
        print(f"Missing OAuth client file: {CREDENTIALS_FILE}")
        print("Put the downloaded Google OAuth JSON here and name it credentials.json.")
        return 1

    config = json.loads(CREDENTIALS_FILE.read_text(encoding="utf-8"))
    if "installed" not in config:
        if "web" in config:
            print("This is a Web application OAuth client. This script expects a Desktop app client.")
            print("Create/download an OAuth client with application type Desktop app, then use that JSON.")
        else:
            print("Unrecognized OAuth JSON. Expected a top-level 'installed' field for a Desktop app client.")
        return 1

    flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
    # Force a fresh consent so the token is issued under the current app status
    # and includes an offline refresh token for subsequent runs.
    credentials = flow.run_local_server(port=0, prompt="consent")
    TOKEN_FILE.write_text(credentials.to_json(), encoding="utf-8")
    TOKEN_FILE.chmod(0o600)

    print(f"Drive authorization succeeded. Token saved to: {TOKEN_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

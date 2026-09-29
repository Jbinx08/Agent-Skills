"""Install Vibe Drive as a global skill for local coding agents."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys
import venv


ROOT = Path(__file__).resolve().parent
SOURCE_SKILL = ROOT / "vibe-drive"
SKILL_NAME = "vibe-drive"
CONFIG = Path.home() / ".vibe-drive"


def copy_private_file(filename: str) -> None:
    source = ROOT / filename
    destination = CONFIG / filename
    if not source.is_file():
        print(f"  {filename}: not found beside installer; existing config kept")
        return
    if destination.exists() and destination.stat().st_mtime >= source.stat().st_mtime:
        print(f"  {filename}: newer config copy kept")
        return
    temporary = CONFIG / f".{filename}.installing"
    shutil.copy2(source, temporary)
    if os.name != "nt":
        temporary.chmod(0o600)
    temporary.replace(destination)
    print(f"  {filename}: copied to private config")


def install_skill(target_root: Path) -> None:
    target = target_root / SKILL_NAME
    if target.is_symlink():
        raise RuntimeError(f"Refusing to replace symlink: {target}")
    if target.exists():
        marker = target / "SKILL.md"
        if not marker.is_file() or "name: vibe-drive" not in marker.read_text(encoding="utf-8")[:300]:
            raise RuntimeError(f"Different skill already exists at {target}")
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_SKILL / "SKILL.md", target / "SKILL.md")
    scripts = target / "scripts"
    scripts.mkdir(exist_ok=True)
    shutil.copy2(SOURCE_SKILL / "scripts" / "vibe_drive.py", scripts / "vibe_drive.py")
    print(f"  installed: {target}")


def main() -> int:
    if sys.version_info < (3, 9):
        print("Python 3.9 or newer is required.", file=sys.stderr)
        return 1
    if not (SOURCE_SKILL / "SKILL.md").is_file():
        print("Skill package is incomplete.", file=sys.stderr)
        return 1

    CONFIG.mkdir(mode=0o700, parents=True, exist_ok=True)
    if os.name != "nt":
        CONFIG.chmod(0o700)
    print("Preparing private Google Drive configuration:")
    copy_private_file("credentials.json")
    copy_private_file("token.json")

    environment = CONFIG / "venv"
    if not environment.exists():
        print("Creating Python environment...")
        venv.EnvBuilder(with_pip=True).create(environment)
    python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    print("Installing Drive API dependencies...")
    subprocess.run(
        [str(python), "-m", "pip", "install", "--disable-pip-version-check", "-r",
         str(ROOT / "requirements.txt")],
        check=True,
    )

    home = Path.home()
    destinations = [
        home / ".codex" / "skills",
        home / ".cursor" / "skills",
        home / ".agent" / "skills",
        home / ".agents" / "skills",
    ]
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        custom_codex = Path(codex_home).expanduser() / "skills"
        if custom_codex not in destinations:
            destinations.append(custom_codex)
    print("Installing global skill:")
    for destination in destinations:
        install_skill(destination)
    if not (CONFIG / "credentials.json").is_file() or not (CONFIG / "token.json").is_file():
        print("Installation completed, but OAuth files are missing. Add credentials.json and run the skill's auth command.")
    else:
        print("Ready. Ask your agent to save or restore a project with Vibe Drive.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        sys.exit(1)

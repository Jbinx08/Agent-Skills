"""Copy the bundled Vibe-master documents into a project without replacing files by default."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil


def apply(target: Path, force: bool = False) -> tuple[int, int]:
    source = Path(__file__).resolve().parent.parent / "assets" / "Vibe-master"
    if not (source / "VIBE_MASTER.md").is_file():
        raise RuntimeError(f"Bundled Vibe-master documents are missing: {source}")
    target = target.expanduser().resolve()
    if target.exists() and not target.is_dir():
        raise ValueError(f"Target must be a directory: {target}")
    destination = target / "Vibe-master"
    if destination == source or source in destination.parents:
        raise ValueError("Target cannot be inside the bundled asset directory")
    destination.mkdir(parents=True, exist_ok=True)
    copied = skipped = 0
    for item in source.rglob("*"):
        if not item.is_file():
            continue
        output = destination / item.relative_to(source)
        if output.exists() and not force:
            skipped += 1
            continue
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, output)
        copied += 1
    if not (destination / "VIBE_MASTER.md").is_file():
        raise RuntimeError("VIBE_MASTER.md was not installed")
    return copied, skipped


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, nargs="?", default=Path.cwd())
    parser.add_argument("--force", action="store_true", help="Replace existing bundled files")
    args = parser.parse_args()
    copied, skipped = apply(args.target, args.force)
    print(f"Vibe Master applied: {args.target.resolve()} (copied: {copied}; kept: {skipped})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Install a self-contained ui-design package at an explicit destination."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import tempfile


SOURCE = Path(__file__).resolve().parents[1] / "skills" / "ui-design"


def install_skill(destination: Path, source: Path = SOURCE) -> Path | None:
    """Replace one package, retaining its previous contents outside skills/."""
    source = source.resolve()
    destination = destination.expanduser()
    if destination.name != "ui-design":
        raise ValueError("Destination must be a directory named ui-design")
    # Resolve parent links, but never follow the destination link when replacing it.
    destination = destination.parent.resolve() / destination.name
    for candidate in (destination, destination.resolve()):
        if candidate == source or candidate in source.parents or source in candidate.parents:
            raise ValueError("Destination must not overlap the canonical source")
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"Source has no SKILL.md: {source}")
    if destination.exists() and not destination.is_dir() and not destination.is_symlink():
        raise ValueError("Destination already exists and is not a package directory")

    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".ui-design-install-", dir=destination.parent))
    staged_package = staging / "ui-design"
    backup = None
    try:
        # Dereference repository links so installed packages are independent copies.
        shutil.copytree(source, staged_package, symlinks=False)
        if not (staged_package / "SKILL.md").is_file():
            raise ValueError("Staged package has no SKILL.md")
        if destination.exists() or destination.is_symlink():
            backup_root = destination.parent.parent / "skill-backups"
            backup_root.mkdir(parents=True, exist_ok=True)
            backup_dir = Path(tempfile.mkdtemp(prefix="ui-design-", dir=backup_root))
            backup = backup_dir / "ui-design"
            os.replace(destination, backup)
        try:
            os.replace(staged_package, destination)
        except BaseException:
            if backup is not None:
                try:
                    os.replace(backup, destination)
                except OSError as error:
                    raise RuntimeError(
                        f"Install and restoration failed; previous package remains at {backup}"
                    ) from error
                backup.parent.rmdir()
            raise
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return backup


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="Explicit package path ending in ui-design")
    args = parser.parse_args()
    try:
        backup = install_skill(args.destination)
    except (OSError, ValueError, RuntimeError, shutil.Error) as error:
        parser.exit(1, f"Install failed: {error}\n")
    print(f"Installed ui-design: {args.destination.expanduser()}")
    if backup is not None:
        print(f"Previous package backed up: {backup}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Create a new folder with naming convention:
  todaysTasks_XXXXXX_YYYY-MM-DD

- XXXXXX is a zero-padded sequence that increments each run
- YYYY-MM-DD is the current date

Usage:
  python tools/create_todays_tasks.py

The folder is created in the current working directory and the path is printed.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path


def next_sequence(base: Path) -> int:
    pattern = re.compile(r"^todaysTasks_(\d{6})_\d{4}-\d{2}-\d{2}$")
    max_seq = 0
    for p in base.iterdir():
        if p.is_dir():
            m = pattern.match(p.name)
            if m:
                try:
                    seq = int(m.group(1))
                    if seq > max_seq:
                        max_seq = seq
                except ValueError:
                    continue
    return max_seq + 1


def main() -> None:
    cwd = Path.cwd()
    today = datetime.now().strftime("%Y-%m-%d")
    seq = next_sequence(cwd)

    # ensure uniqueness if sequence already exists for some reason
    while True:
        folder_name = f"todaysTasks_{seq:06d}_{today}"
        target = cwd / folder_name
        if not target.exists():
            break
        seq += 1

    target.mkdir(parents=True, exist_ok=False)

    # optional: write a small note inside
    info = target / "README.md"
    info.write_text(
        f"# Today\'s Tasks\n\nCreated: {datetime.now().isoformat(timespec='seconds')}\n\n",
        encoding="utf-8",
    )

    print(str(target.resolve()))


if __name__ == "__main__":
    main()


"""Print line, word, and character counts for a text file as JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def count_text_stats(contents: str) -> dict[str, int]:
    return {
        "lines": len(contents.splitlines()),
        "words": len(contents.split()),
        "characters": len(contents),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a text file."
    )
    parser.add_argument("file_path", help="path to the text file")
    args = parser.parse_args(argv)

    try:
        contents = Path(args.file_path).read_text(encoding="utf-8")
    except FileNotFoundError:
        payload = {
            "error": f"File not found: {args.file_path}",
            "lines": 0,
            "words": 0,
            "characters": 0,
        }
        print(json.dumps(payload))
        return 1
    except OSError as exc:
        payload = {
            "error": str(exc),
            "lines": 0,
            "words": 0,
            "characters": 0,
        }
        print(json.dumps(payload))
        return 1

    print(json.dumps(count_text_stats(contents)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

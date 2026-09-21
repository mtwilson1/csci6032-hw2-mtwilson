"""Print line, word, and character counts for a text file as JSON."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path


def nonnegative_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be non-negative")
    return number


def count_text_stats(contents: str, top: int | None = None) -> dict:
    stats = {
        "lines": len(contents.splitlines()),
        "words": len(contents.split()),
        "characters": len(contents),
    }
    if top is not None:
        counts = Counter(word.casefold() for word in contents.split())
        stats["top_words"] = [
            {"word": word, "count": count}
            for word, count in sorted(
                counts.items(), key=lambda item: (-item[1], item[0])
            )[:top]
        ]
    return stats


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a text file."
    )
    parser.add_argument("file_path", help="path to the text file")
    parser.add_argument(
        "--top",
        type=nonnegative_int,
        help="include the N most frequent words",
    )
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

    print(json.dumps(count_text_stats(contents, top=args.top)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Print line, word, and character counts for a text file."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a text file."
    )
    parser.add_argument("file_path", help="path to the text file")
    args = parser.parse_args()

    try:
        with open(args.file_path, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Error: file not found: {args.file_path}")
        return

    print(f"Lines: {len(contents.splitlines())}")
    print(f"Words: {len(contents.split())}")
    print(f"Characters: {len(contents)}")


if __name__ == "__main__":
    main()

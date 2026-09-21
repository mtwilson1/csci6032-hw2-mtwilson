import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "src" / "text_stats.py"
SAMPLE = ROOT / "sample.txt"


class TextStatsTests(unittest.TestCase):
    def run_script(self, file_path, *arguments):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *arguments, str(file_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        return result

    def test_sample_file_counts(self):
        result = self.run_script(SAMPLE)

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        payload = json.loads(result.stdout)

        self.assertEqual(
            payload,
            {"lines": 5, "words": 44, "characters": 235},
        )

    def test_missing_file_reports_json_error(self):
        missing_path = ROOT / "missing.txt"
        result = self.run_script(missing_path)

        self.assertEqual(result.returncode, 1)
        payload = json.loads(result.stdout)

        self.assertIn("lines", payload)
        self.assertIn("words", payload)
        self.assertIn("characters", payload)
        self.assertIn("error", payload)

    def test_count_text_stats_for_custom_text(self):
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as handle:
            handle.write("one two\nthree\n")
            temp_path = Path(handle.name)

        try:
            result = self.run_script(temp_path)
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload, {"lines": 2, "words": 3, "characters": 14})
        finally:
            temp_path.unlink(missing_ok=True)

    def test_top_words_are_case_insensitive_and_tie_broken_alphabetically(self):
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as handle:
            handle.write("Banana apple BANANA cherry Apple")
            temp_path = Path(handle.name)

        try:
            result = self.run_script(temp_path, "--top", "3")
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(
                payload["top_words"],
                [
                    {"word": "apple", "count": 2},
                    {"word": "banana", "count": 2},
                    {"word": "cherry", "count": 1},
                ],
            )
        finally:
            temp_path.unlink(missing_ok=True)

    def test_top_zero_reports_no_words(self):
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as handle:
            handle.write("one two")
            temp_path = Path(handle.name)

        try:
            result = self.run_script(temp_path, "--top", "0")
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            self.assertEqual(json.loads(result.stdout)["top_words"], [])
        finally:
            temp_path.unlink(missing_ok=True)

    def test_negative_top_is_rejected(self):
        result = self.run_script(SAMPLE, "--top", "-1")

        self.assertEqual(result.returncode, 2)
        self.assertIn("must be non-negative", result.stderr)


if __name__ == "__main__":
    unittest.main()

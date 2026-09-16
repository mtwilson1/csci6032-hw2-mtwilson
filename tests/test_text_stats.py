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
    def run_script(self, file_path):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(file_path)],
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


if __name__ == "__main__":
    unittest.main()

# csci6032-hw2-mtwilson

## Text stats utility

The project includes a command-line script at `src/text_stats.py` that reads a text file and reports the number of lines, words, and characters as JSON.

### Usage

Run the script with a file path:

```bash
python3 src/text_stats.py sample.txt
```

Example output:

```json
{"lines": 5, "words": 44, "characters": 235}
```

The script exits with status code 1 and prints a JSON error message if the file cannot be found.

### Running tests

```bash
python3 -m unittest discover -s tests
```
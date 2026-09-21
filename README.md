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

To include the most frequent words, pass a non-negative count with `--top`:

```bash
python3 src/text_stats.py --top 3 sample.txt
```

The output includes a `top_words` array of objects containing each word and its
count. Words are compared case-insensitively and returned in descending
frequency order, with alphabetical order used to break ties. The words in
`top_words` are lowercase.

The script exits with status code 1 and prints a JSON error message if the file cannot be found.

### Running tests

```bash
python3 -m unittest discover -s tests
```
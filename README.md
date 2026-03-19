# Steam Discount Scraper

A command-line tool that scrapes free and discounted games from the Steam store.

## Requirements

- Python 3
- `beautifulsoup4`

Install dependencies:

```bash
pip install beautifulsoup4
```

## Usage

```bash
python main.py [options]
```

### Options

| Flag | Description |
|------|-------------|
| `-l`, `--list` | Print the names of all found games |
| `-h`, `--help` | Show help message and exit |

### Examples

Print only the amount of results:
```bash
python main.py
```

Print the amount of results and list all game names:
```bash
python main.py --list
```

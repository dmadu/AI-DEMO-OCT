# App

A minimal, self-contained Python command line application scaffold.

## Requirements

- Python 3.9+

## Usage

```bash
python src/app.py --name World
python src/app.py --name Ada --repeat 3
```

### Options

| Option | Description | Default |
| --- | --- | --- |
| `-n`, `--name` | Name to greet | `World` |
| `-r`, `--repeat` | Number of times to print the greeting | `1` |
| `-h`, `--help` | Show help and exit | - |

## Tests

```bash
pip install pytest
pytest
```

## Project layout

```
.
├── README.md
├── src
│   └── app.py
└── tests
    └── test_app.py
```

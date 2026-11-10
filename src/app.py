"""Application entry point.

A small, self-contained command line application scaffold.
Run with:

    python src/app.py --name World
"""

from __future__ import annotations

import argparse
import sys
from typing import Sequence


def greet(name: str) -> str:
    """Return a greeting for the given name.

    Args:
        name: The name to greet. Falls back to "World" when empty.

    Returns:
        A greeting string.
    """
    cleaned = (name or "").strip() or "World"
    return f"Hello, {cleaned}!"


def build_parser() -> argparse.ArgumentParser:
    """Create the command line argument parser."""
    parser = argparse.ArgumentParser(
        prog="app",
        description="A minimal command line application.",
    )
    parser.add_argument(
        "-n",
        "--name",
        default="World",
        help="Name to greet (default: %(default)s)",
    )
    parser.add_argument(
        "-r",
        "--repeat",
        type=int,
        default=1,
        help="How many times to print the greeting (default: %(default)s)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Program entry point.

    Args:
        argv: Optional argument vector (defaults to ``sys.argv[1:]``).

    Returns:
        Process exit code.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.repeat < 1:
        parser.error("--repeat must be a positive integer")

    message = greet(args.name)
    for _ in range(args.repeat):
        print(message)

    return 0


if __name__ == "__main__":
    sys.exit(main())

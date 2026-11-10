"""Tests for the application scaffold."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import greet, main  # noqa: E402


def test_greet_default():
    assert greet("") == "Hello, World!"


def test_greet_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_strips_whitespace():
    assert greet("  Ada  ") == "Hello, Ada!"


def test_main_returns_zero(capsys):
    exit_code = main(["--name", "Ada", "--repeat", "2"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "Hello, Ada!\nHello, Ada!\n"

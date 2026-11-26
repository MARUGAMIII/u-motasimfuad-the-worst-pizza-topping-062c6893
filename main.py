#!/usr/bin/env python3
"""The Worst Pizza Topping -- make.fun entry.

Writes one funny line, under 200 characters, pitching a terrible
pizza topping, to /output/entry.txt. Standard library only,
deterministic: the same line every run.
"""

from pathlib import Path

ENTRY = (
    "Our new pizza topping is magnets: they stick to your "
    "fillings, your braces, and move in with the fridge."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.isascii(), "entry must be plain ASCII"
    assert "\n" not in ENTRY, "entry must be a single line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

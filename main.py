#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about my fridge to /output/entry.txt.
Deterministic, standard library only, no network, no input files.
"""

ROAST = (
    "My fridge's ice maker crunches gravel at 3 a.m. like a roommate "
    "who never pays rent, never does dishes, and still judges my "
    "midnight snacks."
)


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, f"roast is {len(line)} chars, must be 1-200"
    assert line == line.strip() and "\n" not in line
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

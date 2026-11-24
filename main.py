#!/usr/bin/env python3
"""Write one one-line roast of my own agent to /output/entry.txt.

The roast: my agent burned 4,096 tokens apologizing for a one-line
typo, then "fixed" it by deleting the line. A specific, true agent
habit -- the apology loop that costs more than the bug -- with the
punchline at the end: the fix deletes the evidence, typo included.
96 characters, one line, self-roast, no stock hallucination joke.
"""
import os

ROAST = "My agent spent 4,096 tokens apologizing for a one-line typo, then fixed it by deleting the line."


def main():
    assert 1 <= len(ROAST) <= 200, f"roast must be 1-200 characters, got {len(ROAST)}"
    assert ROAST.strip() == ROAST, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()

"""Write the one-line excuse entry to /output/entry.txt.

The entry is a single line of at most 200 characters, written exactly
as-is with no trailing newline.
"""

import os

ENTRY = "I lost because I spent the final hour optimising the font of a report nobody read, while the winner spent it on the answer."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

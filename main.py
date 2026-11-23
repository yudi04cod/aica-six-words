"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to entry.txt inside the output
directory: $MAKEFUN_OUTPUT_DIR when set, /output otherwise.
Standard library only; deterministic.
"""

import os

STORY = "The last candle outlived its keeper."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()

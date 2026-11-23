"""One Line, Zero Use entry program (stdlib only).

Writes the single entry line, byte-exact, to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output) and prints it.
No network, no randomness, no third-party imports.
"""

import os
import sys

LINE = "I can make any queue move faster, but only the one I'm not standing in."

# Gate: the entry must be 1-200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
assert LINE.strip() == LINE and LINE.strip(), "entry line must not be blank"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

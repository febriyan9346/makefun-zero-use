"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (<=200 chars) describing a hilariously
useless superpower to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = "I can talk to the dead, but they only ever want to complain about the Wi-Fi."

assert 1 <= len(LINE) <= 200, len(LINE)
assert LINE.strip(), "line must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

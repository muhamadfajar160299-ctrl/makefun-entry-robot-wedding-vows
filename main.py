"""One-line robot wedding vows entry.

Reads the single-line vow shipped beside this script (entry.txt) and
copies it byte-identically into $MAKEFUN_OUTPUT_DIR/entry.txt with mode
0644. Standard library only; no network, no temp files.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, "entry.txt")
    try:
        with open(src_path, "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"cannot read {src_path}: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if not data.strip():
        print("entry.txt is empty or only whitespace", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        raise SystemExit(1)
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "wb") as f:
            f.write(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

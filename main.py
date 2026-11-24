"""One Word, First Thought — entry program.

Writes exactly one word, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), as the
bounty's RULES.txt requires. Deterministic: no randomness, no network,
no input files.

The word: defenestration — the act of throwing someone out of a
window. Vivid, surprising, and funny: a whole dramatic scene packed
into one word, with a story the judge cannot help picturing. The
field is crowded with pretty nature words (petrichor four times over,
murmuration, apricity, susurrus); this one is the opposite angle —
wit and a little violence instead of another soft landscape.
"""

import os

WORD = "defenestration"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {path} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()

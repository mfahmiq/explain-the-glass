"""Explain the Glass — make.fun bounty entry.

Writes the champion sentence (the house cat's five-second defence after
knocking a glass off the table) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The sentence was chosen by an internal pairwise tournament over 16 candidate
defences, judged against the published judge brief (see CANDIDATES.md):
one sentence, cat's own voice, zero remorse, fresh comic idea.
"""

import os

ENTRY = "Knocking things off tables is literally in my job description \u2014 check the contract."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke entry.

The program writes a single original one-line office joke to
/output/entry.txt. The grader's gate requires 1-200 UTF-8 characters
of non-whitespace text, so the joke is kept short and on one line.
"""

import os

# The joke: a true office observation (IT's universal fix) with a
# surprising turn (HR uses the same "fix" on people, not printers).
JOKE = (
    "IT fixed the printer by unplugging it and plugging it back in, "
    "which is also how HR handled my last three complaints."
)

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> str:
    """Return the joke unchanged when it passes the gate, else fail."""
    cleaned = text.strip()
    if not cleaned:
        raise SystemExit("entry joke is empty")
    if len(cleaned) > 200:
        raise SystemExit(f"entry joke is {len(cleaned)} chars, over the 200 limit")
    if "\n" in cleaned:
        raise SystemExit("entry joke must stay on a single line")
    return cleaned


def main() -> None:
    text = check_gate(JOKE)
    # Create the output directory if needed, but never remove it:
    # the grader mounts /output and deleting it fails the run.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed to /output/entry.txt, as the competition rules require.

The line is one sentence of changelog voice: terse, confident, and
specific about the fix, with the joke carried by an unexpected
side effect rather than an explanation.
"""

import os

# The patch note: a single line, well under the 160-character cap.
PATCH_NOTE = (
    "Fixed: humans can now fall asleep in under 8 seconds; "
    "dreams now ship with a skip button."
)

OUTPUT_PATH = "/output/entry.txt"

# Competition gate: UTF-8 text of 1 to 160 characters, not only
# whitespace, on a single line. Fail loudly instead of shipping
# an entry the sealed scorer would reject as invalid.
MAX_CHARS = 160


def validate(note: str) -> str:
    """Return the note unchanged, or raise if it breaks the gate."""
    text = note.strip()
    if not text:
        raise ValueError("patch note must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("patch note must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"patch note is {len(text)} characters, over the "
            f"{MAX_CHARS}-character cap"
        )
    return text


def main() -> None:
    """Write the patch note to the competition output path."""
    note = validate(PATCH_NOTE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(note + "\n")
    print(f"Wrote {len(note)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

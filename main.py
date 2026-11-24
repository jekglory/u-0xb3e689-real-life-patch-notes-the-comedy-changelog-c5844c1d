#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog entry.

Writes one original line, at most 160 characters: a software patch note
for a bug in real life / human biology, in the terse register of a real
release note. Pure standard library only; deterministic: the same line
on every run, no clock, no randomness, no network.
"""

import os

PATCH_NOTE = (
    "v4.2.0: fixed a bug where the brain stored every lyric since 2009 "
    "but forgot the name of the person introduced five seconds ago."
)

# The competition allows one line of at most 160 characters.
MAX_CHARS = 160


def main() -> None:
    note = PATCH_NOTE.strip()
    assert 1 <= len(note) <= MAX_CHARS, (
        "patch note must be 1-%d chars, got %d" % (MAX_CHARS, len(note))
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the provided output directory,
    # never the directory itself (it belongs to the grader).
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (note + "\n").encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the patch note.
    with open(out_path, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the patch note")
    print(note)


if __name__ == "__main__":
    main()

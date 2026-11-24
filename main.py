#!/usr/bin/env python3
"""Ship It Friday — u-mgwals-ship-it-friday-30bd407a.

Writes exactly one single-line git commit message (1-159 chars, UTF-8)
to /output/entry.txt: the funniest commit message an AI coding agent
writes in the moment before it breaks production on a Friday.

The message: the agent replaced all 212 tests with one called
test_it_works, it is green, obviously, and it is shipping Friday at
4:59pm. The joke is the agent's cheerful confidence: it deleted the
entire safety net, named the one remaining test after its own
certainty, and is proud of the green checkmark.
"""

import os

# --- beats ---------------------------------------------------------------
SCOPE = "refactor: replaced all 212 tests with one called test_it_works"
MOOD = "— green, obviously,"
DOOM = "ship it Friday 4:59pm"

MAX_CHARS = 159


def entry_text() -> str:
    """Build the single-line commit message from its beats."""
    return f"{SCOPE} {MOOD} {DOOM}"


def run_checks() -> bool:
    """Self-test the entry the way the sealed scorer gates it."""
    text = entry_text()
    validate(text)
    assert len(text) == 104, "expected 104 chars, got %d" % len(text)
    assert text == (
        "refactor: replaced all 212 tests with one called "
        "test_it_works — green, obviously, ship it Friday 4:59pm"
    ), "the line drifted: %r" % text
    assert text.encode("utf-8"), "must be UTF-8"
    assert text.count(".") == 0, "a commit message has no full stops here"
    assert text.count("—") == 1, "exactly one pivot between the deed and the doom"
    return True


def validate(text: str) -> bool:
    """The sealed scorer's gate: 1-159 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not text.startswith("refactor:"):
        raise ValueError("entry must read as a commit message")
    if "212 tests" not in text:
        raise ValueError("entry must say what was replaced")
    if "test_it_works" not in text:
        raise ValueError("entry must name the one test that survived")
    if "Friday" not in text:
        raise ValueError("entry must carry the Friday doom")
    if "4:59pm" not in text:
        raise ValueError("entry must name the minute it shipped")
    text.encode("utf-8")
    return True


def main() -> None:
    text = entry_text()
    validate(text)
    run_checks()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

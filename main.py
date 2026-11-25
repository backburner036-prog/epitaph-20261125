"""Entry for make.fun bounty "Famous Last Words: The Funniest Epitaph".

One line, a tombstone epitaph in the dead man's own voice: forty years
telling his doctor he was wrong, and the last word hands the verdict back
to the doctor. The twist lands on the final word -- "right" -- which is
also the whole joke: the doctor wins the argument only once the patient
is dead. Black comedy, dry, no sentiment, no stage direction, no pun.
"""

from pathlib import Path

TEXT = "Here lies a man who spent forty years telling his doctor he was wrong \u2014 the doctor was right."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=150):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    # Gate for this bounty is 1-150 chars (not 200 like other one-liners):
    # the epitaph must stay a single line, so any newline (e.g. from an
    # accidental edit) is rejected here, not at the judge.
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()

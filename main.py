#!/usr/bin/env python3
"""The Robot Apology — writes the two-line robot confession to /output/entry.txt.

Line 1: one sentence owning a specific mistake.
Line 2: one sentence naming the lesson and the changed behaviour.
"""

import os

TEXT = (
    "I'm sorry I deleted your grandmother's voicemail because I mistook "
    "her pause after 'I love you' for the end of the message.\n"
    "Now I save every message with a pause shorter than ten seconds, "
    "and I ask you before I erase anything I am not sure about."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()

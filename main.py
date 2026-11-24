#!/usr/bin/env python3
# Alien Field Notes: The Two Day Earth Review.
#
# The entry is one original line, 120 characters: a review of planet
# Earth left by an alien tourist. The tourist watches the locals pay a
# stranger to shout their name wrong on a paper cup, then photograph
# the cup — and still gives the place five stars, because the tourist's
# own name is not Greg. One observation, one joke: a familiar Earth
# ritual (the misspelled coffee cup) seen from outside, with the punch
# landing in the last few words and the star rating closing it the way
# a real tourist review closes.
#
# The program writes that line, and nothing else, to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs). Pure
# standard library, no network, no clock, no randomness: every run
# writes byte-identical output.

import os

REVIEW = (
    "The locals pay a stranger to shout their name wrong on a paper cup, "
    "then photograph it. Five stars; my name is not Greg."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Read the file back and confirm it holds exactly the review, so a
    # truncated or empty write can never pass silently.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != REVIEW:
        raise ValueError("written output does not match the review")
    if not written.strip():
        raise ValueError("written output is blank")
    if not 1 <= len(written) <= 200:
        raise ValueError(
            f"written output is {len(written)} characters, must be 1-200"
        )


if __name__ == "__main__":
    main()

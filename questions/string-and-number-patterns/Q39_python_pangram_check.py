"""
QUESTION:
Determine whether a sentence is a pangram.

CONCEPT:
Sets, alphabet coverage.

DIFFICULTY:
Beginner

APPROACH:
Convert the string to lowercase and test whether all letters of the alphabet are present.

EXAMPLE RUN:
is_pangram("The quick brown fox jumps over the lazy dog") == True
"""


def is_pangram(text: str) -> bool:
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(text.lower())


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))

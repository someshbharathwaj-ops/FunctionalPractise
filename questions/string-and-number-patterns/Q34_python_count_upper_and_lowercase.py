"""
QUESTION:
Count uppercase and lowercase letters in a string.

CONCEPT:
Predicate-based counting, generator expressions.

DIFFICULTY:
Beginner

APPROACH:
Count uppercase and lowercase characters independently with `sum`.

EXAMPLE RUN:
count_case("The quick Brow Fox") == (3, 13)
"""


def count_case(text: str) -> tuple[int, int]:
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return upper, lower


if __name__ == "__main__":
    print(count_case("The quick Brow Fox"))

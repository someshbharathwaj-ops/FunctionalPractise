"""
QUESTION:
Given a list of integers, return the even, odd, positive, negative, and zero values as separate
groups.

CONCEPT:
Filtering, multi-view analysis.

DIFFICULTY:
Beginner

APPROACH:
Build each category with its own `filter` predicate.

EXAMPLE RUN:
([2, 4, 6], [1, 3, 5], [1, 2, 3, 4, 5, 6], [], [0])
"""


def classify_numbers(values: list[int]) -> tuple[list[int], list[int], list[int], list[int], list[int]]:
    even = list(filter(lambda x: x % 2 == 0, values))
    odd = list(filter(lambda x: x % 2 != 0, values))
    positive = list(filter(lambda x: x > 0, values))
    negative = list(filter(lambda x: x < 0, values))
    zero = list(filter(lambda x: x == 0, values))
    return even, odd, positive, negative, zero


if __name__ == "__main__":
    print(classify_numbers([0, 1, 2, 3, 4, 5, 6]))

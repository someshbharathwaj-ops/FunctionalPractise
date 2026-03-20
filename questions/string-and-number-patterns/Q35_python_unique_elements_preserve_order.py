"""
QUESTION:
Return the unique elements of a list while preserving their first-occurrence order.

CONCEPT:
Reduction, order-preserving deduplication.

DIFFICULTY:
Intermediate

APPROACH:
Use `reduce` to accumulate only unseen values.

EXAMPLE RUN:
unique_list([1,2,3,3,4,5,5]) == [1,2,3,4,5]
"""

from functools import reduce


def unique_list(values: list[int]) -> list[int]:
    return reduce(
        lambda acc, value: acc if value in acc else acc + [value],
        values,
        [],
    )


if __name__ == "__main__":
    print(unique_list([1, 2, 3, 3, 4, 5, 5]))

"""
QUESTION:
Use `reduce` to aggregate a list of integers with a supplied binary operation such as addition or
multiplication.

CONCEPT:
Reduction, higher-order functions.

DIFFICULTY:
Beginner

APPROACH:
Pass the operation into a reusable helper built on `functools.reduce`.

EXAMPLE RUN:
Sum: 15
Product: 120
"""

from functools import reduce


def operate_on_list(values: list[int], operation) -> int:
    return reduce(operation, values)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Sum:", operate_on_list(numbers, lambda left, right: left + right))
    print("Product:", operate_on_list(numbers, lambda left, right: left * right))

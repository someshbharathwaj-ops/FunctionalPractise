"""
QUESTION:
Generate all ordered pairs `(x, y)` for `x` and `y` from 1 to 10 such that `x + y` is prime.

CONCEPT:
List comprehensions, helper predicates, combinatorial generation.

DIFFICULTY:
Intermediate

APPROACH:
Use a primality helper and a nested comprehension to generate all valid ordered pairs.

EXAMPLE RUN:
[(1, 1), (1, 2), (1, 4), (1, 6), (1, 10), (2, 1), (2, 3), (2, 5), (2, 9), (3, 2), (3, 4), (3, 8), (3, 10), (4, 1), (4, 3), (4, 7), (4, 9), (5, 2), (5, 6), (5, 8), (6, 1), (6, 5), (6, 7), (7, 4), (7, 6), (7, 10), (8, 3), (8, 5), (8, 9), (9, 2), (9, 4), (9, 8), (9, 10), (10, 1), (10, 3), (10, 7), (10, 9)]

NOTES:
This comes directly from the list-comprehension practice questions and is preserved as a generator-style exercise.
"""


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    return all(number % divisor != 0 for divisor in range(2, int(number**0.5) + 1))


def prime_sum_pairs(limit: int) -> list[tuple[int, int]]:
    return [
        (left, right)
        for left in range(1, limit + 1)
        for right in range(1, limit + 1)
        if is_prime(left + right)
    ]


if __name__ == "__main__":
    print(prime_sum_pairs(10))

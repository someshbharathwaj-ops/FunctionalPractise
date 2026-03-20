"""
QUESTION:
Determine whether a number is perfect by summing its proper divisors.

CONCEPT:
Divisor generation, numeric predicates.

DIFFICULTY:
Intermediate

APPROACH:
Generate all positive divisors smaller than the number and compare their sum with the number itself.

EXAMPLE RUN:
is_perfect(6) == True
"""


def is_perfect(number: int) -> bool:
    divisors = [divisor for divisor in range(1, number) if number % divisor == 0]
    return sum(divisors) == number


if __name__ == "__main__":
    print(is_perfect(6))

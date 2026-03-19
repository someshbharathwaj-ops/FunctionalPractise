"""
QUESTION:
Generate the first `n` rows of Pascal's triangle in a functional style.

CONCEPT:
Recursion, list construction, adjacent-pair summation.

DIFFICULTY:
Intermediate

APPROACH:
Build the triangle row by row. Each new row is derived from the previous row by adding adjacent
pairs and padding the ends with 1.

EXAMPLE RUN:
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

NOTES:
The source practice file used imperative loops. This version keeps the same question but reframes it
as a recursive functional construction.
"""


def next_row(row: list[int]) -> list[int]:
    if not row:
        return [1]
    middle = list(map(lambda pair: pair[0] + pair[1], zip(row, row[1:])))
    return [1] + middle + [1]


def pascal_triangle(rows: int) -> list[list[int]]:
    def build(remaining: int, previous: list[int], triangle: list[list[int]]) -> list[list[int]]:
        if remaining == 0:
            return triangle

        current = next_row(previous)
        return build(remaining - 1, current, triangle + [current])

    return build(rows, [], [])


if __name__ == "__main__":
    print(pascal_triangle(5))

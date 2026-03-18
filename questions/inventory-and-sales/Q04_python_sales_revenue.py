"""
QUESTION:
Given a list of sales entries as (product, quantity, unit_price), remove invalid records, compute
total revenue, and identify the product with the highest price.

CONCEPT:
Filtering, mapping, reduction, immutable data cleaning.

DIFFICULTY:
Intermediate

APPROACH:
The pipeline first cleans invalid rows, then derives revenue and the highest-priced product from the
sanitized list. The implementation uses `filter`, `map`, and `reduce` instead of manual indexing.

EXAMPLE RUN:
Cleaned sales: [('Laptop', 2, 800), ('Smartphone', 1, 500), ('Headphones', 5, 50), ('Laptop', 1, 800), ('Smartwatch', 3, 150), ('Headphones', 3, 50)]
Total Sales Revenue: 3750
Highest Price Product: ('Laptop', 800)

NOTES:
Rows with an empty product name, non-positive quantity, or non-positive price are excluded.
"""

from functools import reduce

Sale = tuple[str, int, int]

sample_sales: list[Sale] = [
    ("Laptop", 2, 800),
    ("Smartphone", 1, 500),
    ("Headphones", 5, 50),
    ("Laptop", 1, 800),
    ("Smartwatch", 3, 150),
    ("", 2, 100),
    ("Tablet", -1, 400),
    ("Headphones", 3, 50),
]


def clean_sales(sales: list[Sale]) -> list[Sale]:
    return list(
        filter(lambda sale: sale[0] != "" and sale[1] > 0 and sale[2] > 0, sales)
    )


def total_revenue(sales: list[Sale]) -> int:
    return sum(map(lambda sale: sale[1] * sale[2], sales))


def highest_priced_product(sales: list[Sale]) -> tuple[str, int] | None:
    if not sales:
        return None

    product, _, price = reduce(
        lambda current, candidate: candidate if candidate[2] > current[2] else current,
        sales[1:],
        sales[0],
    )
    return product, price


if __name__ == "__main__":
    cleaned_sales = clean_sales(sample_sales)
    print("Cleaned sales:", cleaned_sales)
    print("Total Sales Revenue:", total_revenue(cleaned_sales))
    print("Highest Price Product:", highest_priced_product(cleaned_sales))

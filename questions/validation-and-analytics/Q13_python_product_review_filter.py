"""
QUESTION:
From a list of product review records, retain only entries with valid positive numeric scores for
quality and usability.

CONCEPT:
Validation, predicate composition, functional filtering.

DIFFICULTY:
Beginner

APPROACH:
The filtering pipeline checks field presence, verifies numeric score types, and excludes non-positive
values. Each stage narrows the list with `filter`.

EXAMPLE RUN:
Valid products: [{'name': 'Laptop', 'quality': 4.5, 'value': 4.2, 'usability': 4.8}]

NOTES:
The original file mixed commented alternatives and redundant checks. This version keeps a single,
clear validation path.
"""

products = [
    {"name": "Laptop", "quality": 4.5, "value": 4.2, "usability": 4.8},
    {"name": "Phone", "quality": 4.0, "value": 3.8},
    {"name": "Camera", "quality": -1, "value": 4.5, "usability": 4.0},
    {"name": "Watch", "quality": "High", "value": 3.5, "usability": 3.0},
]


def valid_products(records: list[dict[str, object]]) -> list[dict[str, object]]:
    with_required_fields = list(
        filter(lambda record: "quality" in record and "usability" in record, records)
    )
    with_numeric_scores = list(
        filter(
            lambda record: isinstance(record["quality"], (int, float))
            and isinstance(record["usability"], (int, float)),
            with_required_fields,
        )
    )
    return list(
        filter(
            lambda record: record["quality"] > 0 and record["usability"] > 0,
            with_numeric_scores,
        )
    )


if __name__ == "__main__":
    print("Valid products:", valid_products(products))

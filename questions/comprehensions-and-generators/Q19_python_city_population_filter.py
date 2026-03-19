"""
QUESTION:
From a list of `(city, population)` tuples, extract the cities whose population is greater than
2,000,000.

CONCEPT:
Filtering tuples, predicate-based selection.

DIFFICULTY:
Beginner

APPROACH:
Use `filter` with a population predicate so the result remains a list of the original tuples.

EXAMPLE RUN:
[('New York', 8500000), ('Los Angeles', 4000000), ('Chicago', 2700000), ('Houston', 2300000)]

NOTES:
This is a cleaned and corrected version of the city-population filter exercise from the practice set.
"""

city_populations = [
    ("New York", 8500000),
    ("Los Angeles", 4000000),
    ("Chicago", 2700000),
    ("Houston", 2300000),
    ("Phoenix", 1600000),
    ("Philadelphia", 1500000),
    ("San Antonio", 1500000),
]


def cities_above_two_million(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return list(filter(lambda city: city[1] > 2_000_000, records))


if __name__ == "__main__":
    print(cities_above_two_million(city_populations))

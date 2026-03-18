"""
QUESTION:
From a patient dataset, retain only valid records for patients older than 40, compute BMI for each
selected patient, and calculate the average BMI across the filtered group.

CONCEPT:
Validation pipelines, map/filter/reduce, derived data in immutable records.

DIFFICULTY:
Intermediate

APPROACH:
Filtering happens in three stages: required fields, valid positive measurements, and the age rule.
BMI values are then added with `map`, and the average is computed with `reduce`.

EXAMPLE RUN:
Average BMI: 27.34
Patients with BMI: [{'name': 'Anna', 'age': 45, 'weight': 70, 'height': 1.6, 'bmi': 27.34}]

NOTES:
The original version mutated dictionaries in place. This refactor returns fresh dictionaries so the
pipeline stays functionally clearer.
"""

from functools import reduce

patients = [
    {"name": "Anna", "age": 45, "weight": 70, "height": 1.6},
    {"name": "Tom", "age": 30, "weight": 80, "height": 1.75},
    {"name": "Sara", "age": 50, "weight": 65},
]

REQUIRED_FIELDS = ("name", "age", "weight", "height")


def valid_patients(records: list[dict[str, float | int | str]]) -> list[dict[str, float | int | str]]:
    present = list(filter(lambda record: all(field in record for field in REQUIRED_FIELDS), records))
    measurable = list(
        filter(
            lambda record: record["age"] > 0
            and record["weight"] > 0
            and record["height"] > 0,
            present,
        )
    )
    return list(filter(lambda record: record["age"] > 40, measurable))


def add_bmi(record: dict[str, float | int | str]) -> dict[str, float | int | str]:
    return {
        **record,
        "bmi": round(record["weight"] / (record["height"] ** 2), 2),
    }


def average_bmi(records: list[dict[str, float | int | str]]) -> float:
    if not records:
        return 0.0

    bmi_values = list(map(lambda record: record["bmi"], records))
    total = reduce(lambda left, right: left + right, bmi_values, 0.0)
    return round(total / len(bmi_values), 2)


if __name__ == "__main__":
    selected_patients = valid_patients(patients)
    patients_with_bmi = list(map(add_bmi, selected_patients))
    print("Average BMI:", average_bmi(patients_with_bmi))
    print("Patients with BMI:", patients_with_bmi)

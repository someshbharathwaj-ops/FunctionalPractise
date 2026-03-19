"""
QUESTION:
Given a list of `(employee_id, score)` tuples, classify each employee as `LOW`, `MEDIUM`, or `HIGH`
based on the score bands below 40, from 40 to 69, and 70 or above.

CONCEPT:
`map`, lambdas, tuple transformation, classification pipelines.

DIFFICULTY:
Beginner

APPROACH:
The solution uses `map` with a small grading function so every input tuple is transformed into a new
tuple containing the employee id and its derived performance label.

EXAMPLE RUN:
[(101, 'LOW'), (102, 'MEDIUM'), (103, 'HIGH'), (104, 'HIGH')]

NOTES:
This refactors a partially written employee-classification exercise from the practice Python file.
"""

EmployeeScore = tuple[int, int]
EmployeeBand = tuple[int, str]

employee_scores: list[EmployeeScore] = [(101, 35), (102, 58), (103, 74), (104, 91)]


def classify_employee_performance(records: list[EmployeeScore]) -> list[EmployeeBand]:
    def band(record: EmployeeScore) -> EmployeeBand:
        employee_id, score = record
        label = "LOW" if score < 40 else "MEDIUM" if score < 70 else "HIGH"
        return employee_id, label

    return list(map(band, records))


if __name__ == "__main__":
    print(classify_employee_performance(employee_scores))

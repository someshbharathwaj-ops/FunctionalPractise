"""
QUESTION:
Given a nested department hierarchy, recursively compute the total organization budget, identify the
department with the highest individual budget, and produce a flattened report of department budgets.

CONCEPT:
Recursion over tree-like data, tuple aggregation, structural decomposition.

DIFFICULTY:
Intermediate

APPROACH:
Each recursive call returns three values for the current subtree: total budget, highest-budget
department, and a flattened list of department summaries. Parent calls combine child results.

EXAMPLE RUN:
Total Budget: 1150000
Highest Budget Department: ('Head Office', 500000)
Flattened Report: [('Head Office', 500000), ('Engineering', 300000), ('Backend', 120000), ('Frontend', 80000), ('Marketing', 150000)]

NOTES:
The original logic was already recursive. The refactor mainly improves naming and keeps the result
shape explicit and easy to test.
"""

Department = dict[str, object]

organization: Department = {
    "name": "Head Office",
    "budget": 500000,
    "subdepartments": [
        {
            "name": "Engineering",
            "budget": 300000,
            "subdepartments": [
                {
                    "name": "Backend",
                    "budget": 120000,
                    "subdepartments": [],
                },
                {
                    "name": "Frontend",
                    "budget": 80000,
                    "subdepartments": [],
                },
            ],
        },
        {
            "name": "Marketing",
            "budget": 150000,
            "subdepartments": [],
        },
    ],
}


def budget_report(
    department: Department,
) -> tuple[int, tuple[str, int], list[tuple[str, int]]]:
    name = str(department["name"])
    budget = int(department["budget"])
    subdepartments = list(department.get("subdepartments", []))

    child_reports = list(map(budget_report, subdepartments))
    total_budget = budget + sum(map(lambda report: report[0], child_reports))
    highest_department = max(
        [(name, budget)] + list(map(lambda report: report[1], child_reports)),
        key=lambda entry: entry[1],
    )
    flattened = [(name, budget)] + [
        department_row
        for _, _, rows in child_reports
        for department_row in rows
    ]

    return total_budget, highest_department, flattened


if __name__ == "__main__":
    total, highest, report = budget_report(organization)
    print("Total Budget:", total)
    print("Highest Budget Department:", highest)
    print("Flattened Report:", report)

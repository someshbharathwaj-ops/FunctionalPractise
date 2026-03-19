"""
QUESTION:
Given a list of sensor readings, remove negative values and square the remaining values.

CONCEPT:
Filtering, mapping, data-cleaning pipelines.

DIFFICULTY:
Beginner

APPROACH:
The pipeline first filters out invalid negative readings and then maps each remaining value to its
square.

EXAMPLE RUN:
[0, 144, 64, 625, 49]

NOTES:
The original practice solution used the bitwise `^` operator by mistake. This version uses numeric
exponentiation and keeps the exercise purely functional.
"""

sensor_readings = [-5, 12, 0, 8, -3, 25, 7]


def transform_sensor_data(readings: list[int]) -> list[int]:
    non_negative = filter(lambda value: value >= 0, readings)
    return list(map(lambda value: value**2, non_negative))


if __name__ == "__main__":
    print(transform_sensor_data(sensor_readings))

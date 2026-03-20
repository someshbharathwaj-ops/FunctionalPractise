"""
QUESTION:
Reverse a string using recursion.

CONCEPT:
Recursion over strings.

DIFFICULTY:
Beginner

APPROACH:
Take the last character and recurse on the remaining prefix until the string is empty.

EXAMPLE RUN:
reverse_string("hello") == "olleh"
"""


def reverse_string(text: str) -> str:
    if text == "":
        return ""
    return text[-1] + reverse_string(text[:-1])


if __name__ == "__main__":
    print(reverse_string("hello"))

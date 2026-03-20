"""
QUESTION:
Check whether a phrase is a palindrome while ignoring spaces and letter case.

CONCEPT:
Normalization, string reversal.

DIFFICULTY:
Beginner

APPROACH:
Normalize the phrase by removing spaces and lowercasing it, then compare it with its reverse.

EXAMPLE RUN:
is_palindrome("Never odd or even") == True
"""


def is_palindrome(text: str) -> bool:
    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]


if __name__ == "__main__":
    print(is_palindrome("Never odd or even"))

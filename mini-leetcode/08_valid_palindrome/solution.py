"""
Problem #8: Valid Palindrome
Difficulty: Easy   Tags: string, two pointers

Given a string, return True if it reads the same forwards and backwards after lowercasing it and ignoring anything that isn't a letter or number.

Examples:
    Input:  s = "A man, a plan, a canal: Panama"
    Output: True
    Input:  s = "race a car"
    Output: False

Stuck? See HINTS.md in this folder.

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

def is_palindrome(s: str) -> bool:
    # TODO: write your solution below
    pass


if __name__ == "__main__":
    # Run this file directly to check your solution against the examples above.
    assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test 1 failed"
    assert is_palindrome("race a car") == False, "Test 2 failed"
    print("All sample tests passed!")

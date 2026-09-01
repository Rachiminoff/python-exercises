"""
Problem #4: Valid Parentheses
Difficulty: Easy   Tags: string, stack

Given a string containing only the characters (){}[], determine whether every opening bracket is closed by the same type of bracket, in the correct order.

Examples:
    Input:  s = "()[]{}"
    Output: True
    Input:  s = "(]"
    Output: False

Stuck? See HINTS.md in this folder.

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

def is_valid(s: str) -> bool:
    # TODO: write your solution below
    pass


if __name__ == "__main__":
    # Run this file directly to check your solution against the examples above.
    assert is_valid("()[]{}") == True, "Test 1 failed"
    assert is_valid("(]") == False, "Test 2 failed"
    print("All sample tests passed!")

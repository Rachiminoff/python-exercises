"""
Problem #7: Reverse String In-Place
Difficulty: Easy   Tags: string, two pointers

Given a list of characters, reverse it in place (don't return a new list — modify the input list directly, using O(1) extra space).

Examples:
    Input:  chars = ["h", "e", "l", "l", "o"]
    Output: ["o", "l", "l", "e", "h"]

Stuck? See HINTS.md in this folder.

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

def reverse_string(chars: list[str]) -> None:
    # TODO: write your solution below
    pass


if __name__ == "__main__":
    # Run this file directly to check your solution against the examples above.
    chars = ["h", "e", "l", "l", "o"]
    reverse_string(chars)
    assert chars == ["o", "l", "l", "e", "h"], "Test 1 failed"
    print("All sample tests passed!")

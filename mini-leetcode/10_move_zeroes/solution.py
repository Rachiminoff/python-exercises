"""
Problem #10: Move Zeroes
Difficulty: Easy   Tags: array, two pointers

Given a list of integers, move all zeroes to the end in place, while keeping the relative order of the non-zero elements. Don't return a new list — modify nums directly.

Examples:
    Input:  nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Stuck? See HINTS.md in this folder.

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

def move_zeroes(nums: list[int]) -> None:
    # TODO: write your solution below
    pass


if __name__ == "__main__":
    # Run this file directly to check your solution against the examples above.
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0], "Test 1 failed"
    print("All sample tests passed!")

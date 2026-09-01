"""
Problem #11: Binary Search
Difficulty: Easy   Tags: array, binary search

Given a sorted list of integers and a target value, return the index of the target if it exists in the list, or -1 if it doesn't. Must run in O(log n) time — no linear scans.

Examples:
    Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
    Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

def binary_search(nums: list[int], target: int) -> int:
    # TODO: write your solution below
    pass


if __name__ == "__main__":
    # Run this file directly to check your solution against the examples above.
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4, "Test 1 failed"
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1, "Test 2 failed"
    print("All sample tests passed!")

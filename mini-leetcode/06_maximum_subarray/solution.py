"""
Problem #6: Maximum Subarray
Difficulty: Easy   Tags: array, dynamic programming (Kadane's)

Given a list of integers (which may include negatives), find the contiguous subarray with the largest sum, and return that sum.

Examples:
    Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6  (subarray [4, -1, 2, 1])
    Input:  nums = [1]
    Output: 1

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

def max_subarray(nums: list[int]) -> int:
    # TODO: write your solution below
    pass


if __name__ == "__main__":
    # Run this file directly to check your solution against the examples above.
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Test 1 failed"
    assert max_subarray([1]) == 1, "Test 2 failed"
    print("All sample tests passed!")

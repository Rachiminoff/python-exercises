"""
Problem #5: Best Time to Buy and Sell Stock
Difficulty: Easy   Tags: array, single pass

Given a list of daily stock prices, find the maximum profit achievable by buying on one day and selling on a later day. Return 0 if no profit is possible.

Examples:
    Input:  prices = [7, 1, 5, 3, 6, 4]
    Output: 5  (buy at 1, sell at 6)
    Input:  prices = [7, 6, 4, 3, 1]
    Output: 0  (prices only fall)

Stuck? See HINTS.md in this folder.

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

def max_profit(prices: list[int]) -> int:
    # TODO: write your solution below
    pass


if __name__ == "__main__":
    # Run this file directly to check your solution against the examples above.
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5, "Test 1 failed"
    assert max_profit([7, 6, 4, 3, 1]) == 0, "Test 2 failed"
    print("All sample tests passed!")

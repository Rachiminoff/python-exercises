"""
Problem #3: Valid Anagram
Difficulty: Easy   Tags: string, hashmap

Given two strings s and t, return True if t is an anagram of s (uses exactly the same letters, same counts, any order), and False otherwise.

Examples:
    Input:  s = "anagram", t = "nagaram"
    Output: True
    Input:  s = "rat", t = "car"
    Output: False

Stuck? See HINTS.md in this folder.

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

def is_anagram(s: str, t: str) -> bool:
    # TODO: write your solution below
    pass


if __name__ == "__main__":
    # Run this file directly to check your solution against the examples above.
    assert is_anagram("anagram", "nagaram") == True, "Test 1 failed"
    assert is_anagram("rat", "car") == False, "Test 2 failed"
    print("All sample tests passed!")

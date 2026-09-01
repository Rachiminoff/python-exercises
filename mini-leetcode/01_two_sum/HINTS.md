# 💡 Hints — Two Sum

*Tags: array, hashmap*

Try the problem for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Brute force is two nested loops (O(n^2)) — can you do it in a single pass instead?
2. Store numbers you've already seen in a dict as {value: index} as you go.
3. For each new number, check whether target - number is already a key in that dict.

## Relevant functions & syntax

`dict`, `enumerate()`, `in (membership test)`

[← back to mini-leetcode](README.md)

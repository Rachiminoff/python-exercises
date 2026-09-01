# 💡 Hints — Maximum Subarray

*Tags: array, dynamic programming (Kadane's)*

Try the problem for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. This is Kadane's Algorithm — it's fine to look up the technique by name, just not this exact answer.
2. At each number, decide: is it better to start a fresh subarray here, or extend the one ending at the previous number?
3. Track two running values: best sum ending exactly at the current position, and the best sum seen anywhere.

## Relevant functions & syntax

`single for loop`, `max()`

[← back to mini-leetcode](README.md)

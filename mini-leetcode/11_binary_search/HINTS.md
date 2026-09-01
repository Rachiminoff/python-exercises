# 💡 Hints — Binary Search

*Tags: array, binary search*

Try the problem for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Keep a low and high index and repeatedly check the midpoint between them.
2. If the middle value is too small, the target must be in the right half — move low up. Too big, move high down.
3. Stop as soon as low > high — that means the target isn't in the list.

## Relevant functions & syntax

`// integer division`, `while loop`

[← back to mini-leetcode](README.md)

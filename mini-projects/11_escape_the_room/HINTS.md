# 💡 Hints — 🚪 Escape the Room

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Sketch the story as a tree on paper first: which choice leads to which outcome, and which single path
   reaches "You escaped!". Code follows naturally once the tree exists.
2. `choice = input("What do you do? ").lower().strip()` — normalize input so "Search The Desk" and
   "search the desk" both work.
3. One `if/elif/else` per decision point. It's fine (expected, even) to have a second one nested inside
   one of the branches for the follow-up choice.
4. Don't worry about handling truly invalid input yet (that's exception handling, later) — an `else:`
   branch that says "Nothing happens." is enough.

## Relevant functions & syntax

`input()`, `.lower()`, `.strip()`, nested `if/elif/else`

[← back to mini-projects](README.md)

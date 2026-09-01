# 💡 Hints — 📓 CLI Journal

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. datetime.date.today() gives you today's date to stamp each entry with.
2. Open the file in append mode: open("journal.txt", "a") — this never erases what's already there.
3. Separate entries with a marker line (like "---") so you can split the file back into a list of entries when reading.
4. To show newest first, reverse the list of entries with slicing: entries[::-1].

## Relevant functions & syntax

`datetime.date.today()`, `open(..., "a")`, `open(..., "r")`, `str.split()`, `list slicing [::-1]`

[← back to mini-projects](README.md)

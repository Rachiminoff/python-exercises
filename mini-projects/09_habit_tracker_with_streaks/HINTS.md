# 💡 Hints — 🔥 Habit Tracker with Streaks

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Store one ISO date string per line in a text file; read them back with open(...).readlines().
2. Convert stored strings back into real dates with datetime.date.fromisoformat().
3. Sort the dates, then walk backward from today counting how many days in a row are exactly 1 day apart (datetime.timedelta(days=1)).

## Relevant functions & syntax

`datetime.date.fromisoformat()`, `datetime.timedelta`, `sorted()`, `open(..., "a")`

[← back to mini-projects](README.md)

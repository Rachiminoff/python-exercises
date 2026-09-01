# 💡 Hints — 🧟 Morse Code Translator

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Build one dict TEXT_TO_MORSE, then reverse it with a dict comprehension: {v: k for k, v in TEXT_TO_MORSE.items()}.
2. Use a single space between Morse letters and something longer, like " / ", between Morse words.
3. Call .upper() on input text before looking it up — Morse code has no concept of case.

## Relevant functions & syntax

`dict comprehension`, `str.split()`, `str.join()`, `str.upper()`

[← back to mini-projects](README.md)

# 💡 Hints — 🤖 Hangman

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Keep guessed letters in a set() — checking membership is O(1) and duplicates don't matter.
2. Build the current display with a list comprehension: [c if c in guessed else "_" for c in word], then " ".join(...) it.
3. You win when every letter in the word is in your guessed set — try set(word) <= guessed.

## Relevant functions & syntax

`random.choice()`, `set`, `in`, `list comprehension`, `str.join()`

[← back to mini-projects](README.md)

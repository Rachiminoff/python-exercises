# 💡 Hints — 🔐 Password Strength Checker & Generator

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Check character categories with str.isupper() / .islower() / .isdigit() run inside any()/all() over the password.
2. For symbols, check any(c in "!@#$%^&*()" for c in password).
3. For generation, pull characters from string.ascii_letters, string.digits, and string.punctuation using random.choice() in a loop, then ''.join() the result.

## Relevant functions & syntax

`len()`, `str.isupper()`, `str.islower()`, `str.isdigit()`, `any()`, `random.choice()`, `string.ascii_letters`, `string.digits`, `string.punctuation`, `str.join()`

[← back to mini-projects](README.md)

# 💡 Hints — 💰 Splitwise-Lite (Bill Splitter)

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Store payments as a dict: {name: amount_paid}.
2. fair_share = sum(payments.values()) / len(payments).
3. Each person's balance = amount_paid - fair_share. Positive means they're owed money; negative means they owe.
4. Sort people by balance with sorted(..., key=...) and match the biggest debtor against the biggest creditor.

## Relevant functions & syntax

`dict`, `sum()`, `len()`, `sorted(key=...)`

[← back to mini-projects](README.md)

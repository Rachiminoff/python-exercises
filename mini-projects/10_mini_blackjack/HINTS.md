# 💡 Hints — 🃏 Mini Blackjack

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. A deck can just be a list of rank strings ("2".."10", "J", "Q", "K", "A") — shuffle it with random.shuffle().
2. Face cards are worth 10; write a helper that sums a hand and treats Ace as 11, then subtracts 10 per Ace if the total goes over 21.
3. Dealer logic is just: while hand_value(dealer) < 17: deal another card.

## Relevant functions & syntax

`random.shuffle()`, `list`, `sum()`, `while loop`

[← back to mini-projects](README.md)

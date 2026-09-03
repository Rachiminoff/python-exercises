"""
Sub-exercise #7.6 — If statements 🤔
Phase 2: Logic & Decisions

Task:
    Given a number 1-6 representing a rolled die, print "Snake eyes!" if it's
    a 1, "Jackpot!" if it's a 6, otherwise just print the number that was
    rolled.

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

# TODO: write your solution below

randomNum = int(input("Enter a number (1-6): "))

if randomNum == 1:
    print("SNAKE EYES!!!")
elif randomNum == 6:
    print("You hit the JACKPOT!")
else:
    print(f"Your number is {randomNum}")

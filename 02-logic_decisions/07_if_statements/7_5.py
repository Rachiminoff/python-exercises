"""
Sub-exercise #7.5 — If statements 🤔
Phase 2: Logic & Decisions

Task:
    Given player_choice and computer_choice (each "rock", "paper", or
    "scissors"), print "Player wins!", "Computer wins!", or "It's a tie!".

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

# TODO: write your solution below

import random

operations = ["(1) Rock\n", "(2) Paper\n", "(3) Scissors\n"]

for i in operations:
    print(i)
    
userChoice = int(input("Enter your choice (1-3): "))

while userChoice < 1 or userChoice > 3:
    print("Invalid choice. Please try again")
    userChoice = int(input("Enter your choice (1-3): "))

computerChoice = random.randint(1, 3)

if computerChoice == 1:
       print("Computer chose Rock\n")
elif computerChoice == 2:
       print("Computer chose Paper\n")
else:
       print("Computer chose Scissors\n") 
       
# rock beats scissors, scissors beats paper, paper beats rock

if (userChoice == 1 and computerChoice == 3) or (userChoice == 2 and computerChoice == 1) or (userChoice == 3 and computerChoice == 2 ):
    print("Player Wins!\n")
elif userChoice == computerChoice:
    print("It's a tie!\n")
else:
    print("Computer Wins!\n")
   
   
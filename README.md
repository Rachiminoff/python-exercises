# 🐍 Python Rehab

A single-track curriculum to shake off vibe-coding brainrot — 34 exercises, in order, ⭐ = mini project checkpoint.

## Rules

- 🚫 **No AI.** No ChatGPT, no Copilot, no autocomplete you didn't type yourself, no pasting the task into a prompt.
- ✅ **Google is fine.** Look up syntax, built-in functions, official docs, Stack Overflow explanations — just don't let anything write the logic for you.

## How to use this repo

1. Go in order — top to bottom, phase by phase. Don't skip to the fun ones.
2. Open the file for the exercise (e.g. `01-fundamentals/01_print_and_comments.py`) and write your solution in it.
3. Run it, make sure it works, then commit:
   ```
   git add .
   git commit -m "Complete #1 - print() & comments"
   ```
4. Check the box below and commit that too. Your commit history becomes your progress log.

## Progress

### Phase 1 — Fundamentals
*The absolute basics: get comfortable with syntax before anything else*

- [ ] **#1** 🖨️ [print() & comments](01-fundamentals/01_print_comments.py)  
      Print a few lines about yourself. Add # comments explaining each one.
- [ ] **#2** ❎ [Variables](01-fundamentals/02_variables.py)  
      Store your name, age, and favorite number in variables, then print a sentence using all three.
- [ ] **#3** 💱 [Type casting](01-fundamentals/03_type_casting.py)  
      Take a number typed as a string and convert it to an int and a float. Try breaking it on purpose with letters.
- [ ] **#4** ⌨️ [User input](01-fundamentals/04_user_input.py)  
      Ask for the user's name and age with input(), then greet them back using both.
- [ ] **#5** 📖 [Mad Libs game](01-fundamentals/05_mad_libs_game.py) **⭐ mini project**  
      Ask for 5-6 words (noun, verb, adjective...) and slot them into a silly pre-written story.

### Phase 2 — Logic & Decisions
*Teach your programs to make choices*

- [ ] **#6** 📐 [Arithmetic & math](02-logic_decisions/06_arithmetic_math.py)  
      Practice +, -, *, /, //, %, ** on a few numbers and predict the output before running it.
- [ ] **#7** 🤔 [If statements](02-logic_decisions/07_if_statements.py)  
      Write a program that checks if a number is positive, negative, or zero.
- [ ] **#8** 🧮 [Calculator program](02-logic_decisions/08_calculator_program.py) **⭐ mini project**  
      Ask for two numbers and an operator (+ - * /), then print the result. Handle divide-by-zero.
- [ ] **#9** 🏋️ [Weight conversion program](02-logic_decisions/09_weight_conversion_program.py) **⭐ mini project**  
      Convert between kg and lbs based on user input and a chosen direction.
- [ ] **#10** 🌡️ [Temperature conversion program](02-logic_decisions/10_temperature_conversion_program.py) **⭐ mini project**  
      Convert between Celsius, Fahrenheit, and Kelvin based on user choice.
- [ ] **#11** 🌦️ [Logical operators](02-logic_decisions/11_logical_operators.py)  
      Write a weather check: print 'stay home' only if it's raining AND windy, using and/or/not.
- [ ] **#12** ❓ [Conditional expressions](02-logic_decisions/12_conditional_expressions.py)  
      Rewrite 3 if/else blocks as one-line ternary expressions (x if cond else y).

### Phase 3 — Strings
*Text manipulation - the thing you'll use constantly and never truly master*

- [ ] **#13** 〰️ [String methods](03-strings/13_string_methods.py)  
      Take a messy string ('  HeLLo WoRLD  ') and clean it up using .strip(), .lower(), .title(), .replace().
- [ ] **#14** ✂️ [String indexing & slicing](03-strings/14_string_indexing_slicing.py)  
      Given a word, print its first letter, last letter, and reverse it using slicing (no loops).
- [ ] **#15** 💬 [Format specifiers (f-strings)](03-strings/15_format_specifiers_f_strings.py)  
      Print a receipt-style line with a name, a price padded to 2 decimals, and a percentage, all via f-strings.

### Phase 4 — Loops
*Repetition - where 'why isn't this stopping' becomes a rite of passage*

- [ ] **#16** ♾️ [While loops](04-loops/16_while_loops.py)  
      Write a loop that keeps asking for a password until the user types 'python123'.
- [ ] **#17** 💵 [Compound interest calculator](04-loops/17_compound_interest_calculator.py) **⭐ mini project**  
      Ask for principal, rate, and years, then loop year by year printing the growing balance.
- [ ] **#18** 🔁 [For loops](04-loops/18_for_loops.py)  
      Loop through a range of 1-20 and print only the odd numbers.
- [ ] **#19** ⌛ [Countdown timer](04-loops/19_countdown_timer.py) **⭐ mini project**  
      Ask for a number of seconds and print a countdown, one number per second using time.sleep().
- [ ] **#20** ➿ [Nested loops](04-loops/20_nested_loops.py)  
      Print a small multiplication table (1-5 by 1-5) using a loop inside a loop.

### Phase 5 — Collections
*Storing more than one thing at a time, properly*

- [ ] **#21** 🍎 [Lists, sets & tuples](05-collections/21_lists_sets_tuples.py)  
      Build a grocery list, add/remove a few items, then explain out loud when you'd use a set or tuple instead.
- [ ] **#22** 🛒 [Shopping cart program](05-collections/22_shopping_cart_program.py) **⭐ mini project**  
      Let the user add items with prices to a cart (list of tuples/dicts) and print a running total.
- [ ] **#23** ⬜ [2D collections](05-collections/23_2d_collections.py)  
      Build a 3x3 grid as a list of lists and print it out like a tic-tac-toe board.
- [ ] **#24** 💯 [Quiz game](05-collections/24_quiz_game.py) **⭐ mini project**  
      Store 5 questions + answers in a list, loop through them, and tally the user's score.
- [ ] **#25** 📙 [Dictionaries](05-collections/25_dictionaries.py)  
      Build a dict of 3 friends -> phone numbers, then let the user look one up by name.
- [ ] **#26** 🍿 [Concession stand program](05-collections/26_concession_stand_program.py) **⭐ mini project**  
      Store a menu as a dict of {item: price}, let the user order multiple items, and print an itemized total.

### Phase 6 — Randomness & Small Games
*This is where it stops feeling like homework*

- [ ] **#27** 🎲 [Random numbers](06-randomness_small_games/27_random_numbers.py)  
      Import random and generate a random int, a random float, and a random choice from a list.
- [ ] **#28** 🔢 [Number guessing game](06-randomness_small_games/28_number_guessing_game.py) **⭐ mini project**  
      Computer picks a random number 1-100, user guesses with higher/lower hints until correct.
- [ ] **#29** 🗿 [Rock, paper, scissors](06-randomness_small_games/29_rock_paper_scissors.py) **⭐ mini project**  
      Play best-of-5 against the computer, tracking the score across rounds.
- [ ] **#30** ⚂ [Dice roller program](06-randomness_small_games/30_dice_roller_program.py) **⭐ mini project**  
      Simulate rolling two dice N times and print how often each total (2-12) came up.

### Phase 7 — Functions & Error Handling
*Structure your code like someone else might have to read it*

- [ ] **#31** 🧰 [Functions & parameters](07-functions_error_handling/31_functions_parameters.py)  
      Turn 3 of your earlier scripts (calculator, temp converter, dice roller) into reusable functions.
- [ ] **#32** 🏧 [ATM program](07-functions_error_handling/32_atm_program.py) **⭐ mini project**  
      Write deposit()/withdraw()/check_balance() functions sharing one balance variable, driven by a menu loop.
- [ ] **#33** ⚠️ [Exceptions & try/except](07-functions_error_handling/33_exceptions_try_except.py)  
      Wrap risky input parsing in try/except so typing letters instead of numbers doesn't crash the program.
- [ ] **#34** 🛡️ [Error-proof calculator](07-functions_error_handling/34_error_proof_calculator.py) **⭐ mini project**  
      Rebuild exercise #8's calculator so it never crashes - bad input, divide-by-zero, everything handled.

---
*34 exercises · 7 phases · no AI allowed.*

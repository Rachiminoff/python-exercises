# Python Rehab

A single-track Python curriculum designed to shake off vibe-coding brainrot and rebuild your programming fundamentals from the ground up.

**34 exercises, completed in order.**  
**Mini project checkpoints are marked with `⭐`.**

The goal isn't to build impressive projects immediately. It's to regain the ability to sit down, read a problem, think through the logic, and write the code yourself.

## Rules

- **No AI.** No ChatGPT, Copilot, AI autocomplete, generated solutions, or pasting the exercise into an AI tool and asking it to write the logic for you.
- **Google is fine.** Look up syntax, built-in functions, official documentation, error messages, and Stack Overflow explanations. Research is allowed; outsourcing the problem-solving isn't.
- **Write the code yourself.** If you find an example online, understand it before using it, and don't copy an entire solution just to make the exercise pass.
- **Don't skip ahead.** The exercises are intentionally ordered so that each phase builds on the previous one.

## How to Use This Repo

1. **Work from top to bottom.** Complete every exercise in order, phase by phase. Don't skip ahead to the fun projects.
2. **Open the exercise file.** For example:
   ```text
   01-fundamentals/01_print_comments.py
   ```
3. **Write your solution in the file.**
4. **Run the program and test it.** Make sure it actually works rather than simply producing the expected output once.
5. **Commit your work.**
   ```bash
   git add .
   git commit -m "Complete #1 - print() & comments"
   ```
6. **Check off the exercise** in this README and commit the progress update as well.

Your Git history becomes your progress log.

## Progress

### Phase 1 — Fundamentals

*The absolute basics. Get comfortable with Python's syntax before moving on.*

- [ ] **#1 — [print() & comments](01-fundamentals/01_print_comments.py)**

  Print a few lines about yourself. Add `#` comments explaining what each line does.

- [ ] **#2 — [Variables](01-fundamentals/02_variables.py)**

  Store your name, age, and favorite number in variables, then print a sentence using all three.

- [ ] **#3 — [Type casting](01-fundamentals/03_type_casting.py)**

  Take a number stored as a string and convert it to an `int` and a `float`. Then deliberately try converting letters and observe what happens.

- [ ] **#4 — [User input](01-fundamentals/04_user_input.py)**

  Ask the user for their name and age using `input()`, then greet them using both values.

- [ ] **#5 — [Mad Libs game](01-fundamentals/05_mad_libs_game.py)** — **⭐ Mini Project**

  Ask the user for 5–6 words (noun, verb, adjective, etc.) and insert them into a silly pre-written story.

### Phase 2 — Logic & Decisions

*Teach your programs how to make decisions.*

- [ ] **#6 — [Arithmetic & math](02-logic_decisions/06_arithmetic_math.py)**

  Practice `+`, `-`, `*`, `/`, `//`, `%`, and `**` using several numbers. Predict the output before running the program.

- [ ] **#7 — [If statements](02-logic_decisions/07_if_statements.py)**

  Write a program that determines whether a number is positive, negative, or zero.

- [ ] **#8 — [Calculator program](02-logic_decisions/08_calculator_program.py)** — **⭐ Mini Project**

  Ask for two numbers and an operator (`+`, `-`, `*`, `/`), then print the result. Make sure division by zero is handled.

- [ ] **#9 — [Weight conversion program](02-logic_decisions/09_weight_conversion_program.py)** — **⭐ Mini Project**

  Convert between kilograms and pounds based on the user's chosen conversion direction.

- [ ] **#10 — [Temperature conversion program](02-logic_decisions/10_temperature_conversion_program.py)** — **⭐ Mini Project**

  Convert between Celsius, Fahrenheit, and Kelvin based on the user's choice.

- [ ] **#11 — [Logical operators](02-logic_decisions/11_logical_operators.py)**

  Write a weather check that prints `"stay home"` only when it is both raining **and** windy. Use `and`, `or`, and `not` in your conditions.

- [ ] **#12 — [Conditional expressions](02-logic_decisions/12_conditional_expressions.py)**

  Rewrite three `if/else` blocks as one-line conditional expressions using the `x if condition else y` syntax.

### Phase 3 — Strings

*Text manipulation: something you'll use constantly and never completely escape.*

- [ ] **#13 — [String methods](03-strings/13_string_methods.py)**

  Take a messy string such as `"  HeLLo WoRLD  "` and clean it up using `.strip()`, `.lower()`, `.title()`, and `.replace()`.

- [ ] **#14 — [String indexing & slicing](03-strings/14_string_indexing_slicing.py)**

  Given a word, print its first character, last character, and reversed version using indexing and slicing. No loops.

- [ ] **#15 — [Format specifiers & f-strings](03-strings/15_format_specifiers_f_strings.py)**

  Print a receipt-style line containing a name, a price formatted to two decimal places, and a percentage. Use f-strings for all formatting.

### Phase 4 — Loops

*Repetition: where "why isn't this stopping?" becomes a rite of passage.*

- [ ] **#16 — [While loops](04-loops/16_while_loops.py)**

  Keep asking the user for a password until they enter `"python123"`.

- [ ] **#17 — [Compound interest calculator](04-loops/17_compound_interest_calculator.py)** — **⭐ Mini Project**

  Ask for a principal amount, interest rate, and number of years. Calculate the balance year by year and print the growing total after each year.

- [ ] **#18 — [For loops](04-loops/18_for_loops.py)**

  Loop through the numbers 1–20 and print only the odd numbers.

- [ ] **#19 — [Countdown timer](04-loops/19_countdown_timer.py)** — **⭐ Mini Project**

  Ask the user for a number of seconds and display a countdown, one number per second, using `time.sleep()`.

- [ ] **#20 — [Nested loops](04-loops/20_nested_loops.py)**

  Generate a small multiplication table from 1×1 through 5×5 using a loop inside another loop.

### Phase 5 — Collections

*Learn how to store and work with more than one piece of data at a time.*

- [ ] **#21 — [Lists, sets & tuples](05-collections/21_lists_sets_tuples.py)**

  Build a grocery list and add and remove several items. Then explain when you would use a list, set, or tuple instead.

- [ ] **#22 — [Shopping cart program](05-collections/22_shopping_cart_program.py)** — **⭐ Mini Project**

  Let the user add items and prices to a shopping cart. Store the data using a list of tuples or dictionaries, then calculate and display the running total.

- [ ] **#23 — [2D collections](05-collections/23_2d_collections.py)**

  Build a 3×3 grid using a list of lists and display it like a tic-tac-toe board.

- [ ] **#24 — [Quiz game](05-collections/24_quiz_game.py)** — **⭐ Mini Project**

  Store five questions and their answers in a collection. Loop through the questions, check the user's answers, and keep track of their score.

- [ ] **#25 — [Dictionaries](05-collections/25_dictionaries.py)**

  Build a dictionary containing three friends and their phone numbers. Let the user look up a friend's number by name.

- [ ] **#26 — [Concession stand program](05-collections/26_concession_stand_program.py)** — **⭐ Mini Project**

  Store a menu as a dictionary of `{item: price}`. Let the user order multiple items and print an itemized bill with the final total.

### Phase 6 — Randomness & Small Games

*This is where it starts feeling less like homework.*

- [ ] **#27 — [Random numbers](06-randomness_small_games/27_random_numbers.py)**

  Import `random` and generate a random integer, a random float, and a random choice from a list.

- [ ] **#28 — [Number guessing game](06-randomness_small_games/28_number_guessing_game.py)** — **⭐ Mini Project**

  Have the computer choose a random number from 1–100. Let the user keep guessing and provide `"higher"` or `"lower"` hints until they get it right.

- [ ] **#29 — [Rock, paper, scissors](06-randomness_small_games/29_rock_paper_scissors.py)** — **⭐ Mini Project**

  Play a best-of-five match against the computer. Track the score across rounds and announce the winner.

- [ ] **#30 — [Dice roller program](06-randomness_small_games/30_dice_roller_program.py)** — **⭐ Mini Project**

  Simulate rolling two dice `N` times and count how often each possible total from 2–12 occurs.

### Phase 7 — Functions & Error Handling

*Structure your code so it can be reused, tested, and understood by someone other than you.*

- [ ] **#31 — [Functions & parameters](07-functions_error_handling/31_functions_parameters.py)**

  Take three earlier programs—the calculator, temperature converter, and dice roller—and refactor them into reusable functions.

- [ ] **#32 — [ATM program](07-functions_error_handling/32_atm_program.py)** — **⭐ Mini Project**

  Write `deposit()`, `withdraw()`, and `check_balance()` functions that operate on a shared balance. Drive the program with a menu loop.

- [ ] **#33 — [Exceptions & try/except](07-functions_error_handling/33_exceptions_try_except.py)**

  Wrap risky input and type conversions in `try/except` blocks so entering letters when a number is expected doesn't crash the program.

- [ ] **#34 — [Error-proof calculator](07-functions_error_handling/34_error_proof_calculator.py)** — **⭐ Mini Project**

  Rebuild exercise #8's calculator so it handles invalid input, unsupported operators, division by zero, and other expected errors without crashing.

---

**34 exercises · 7 phases · no AI allowed.**

The point isn't to finish as quickly as possible.

The point is to reach the end knowing that you can actually write Python again.

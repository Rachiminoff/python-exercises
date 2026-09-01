# 🐍 Python Rehab

A single-track curriculum to shake off vibe-coding brainrot — 34 exercises, in order, ⭐ = mini project checkpoint.
Regular exercises are broken into 3–5 **sub-exercises** (e.g. **2.1**, **2.2**, **2.3**) — each is its own small standalone file, so each concept gets real reps instead of one thin task.

## Rules

- 🚫 **No AI.** No ChatGPT, no Copilot, no autocomplete you didn't type yourself, no pasting the task into a prompt.
- ✅ **Google is fine.** Look up syntax, built-in functions, official docs, Stack Overflow explanations — just don't let anything write the logic for you.

## How to use this repo

1. Go in order — top to bottom, phase by phase. Don't skip to the fun ones.
2. Each numbered exercise is a folder (e.g. `01-fundamentals/02_variables/`). Regular exercises contain one file per sub-exercise (`2_1.py`, `2_2.py`, `2_3.py`, `2_4.py`) — open each, read the task in the docstring, write your solution, run it.
3. ⭐ mini projects are a single `main.py` in their own folder — check off every requirement listed in its docstring before you call it done.
4. Commit as you finish each sub-exercise (or each project):
   ```
   git add .
   git commit -m "Complete 2.3 - swap variables without a temp var"
   ```
5. Check the boxes below and commit that too. Your commit history becomes your progress log.

See [`learning-materials/`](learning-materials/README.md) if you get stuck on a concept — it's organized to match these phases.

## Progress

### Phase 1 — Fundamentals
*The absolute basics: get comfortable with syntax before anything else*

- [ ] **#1** 🖨️ print() & comments
      - [ ] **1.1** [Print "Hello, World!" with a comment above it explaining what print() does.](01-fundamentals/01_print_comments/1_1.py)
      - [ ] **1.2** [Print three separate lines using three separate print() calls.](01-fundamentals/01_print_comments/1_2.py)
      - [ ] **1.3** [Print all three of those lines using a single print() call and \n.](01-fundamentals/01_print_comments/1_3.py)
      - [ ] **1.4** [Write a line of code, then a comment-only line above it explaining why comments never run.](01-fundamentals/01_print_comments/1_4.py)
- [ ] **#2** ❎ Variables
      - [ ] **2.1** [Store your name in a variable and print it inside a sentence.](01-fundamentals/02_variables/2_1.py)
      - [ ] **2.2** [Store your age as a number and print what your age will be in 5 years.](01-fundamentals/02_variables/2_2.py)
      - [ ] **2.3** [Swap the values of two variables without using a third temporary variable.](01-fundamentals/02_variables/2_3.py)
      - [ ] **2.4** [Store your name, age, and favorite number in three variables and print a sentence using all three in one print() call.](01-fundamentals/02_variables/2_4.py)
- [ ] **#3** 💱 Type casting
      - [ ] **3.1** [Convert the string "42" into an int and add 8 to it.](01-fundamentals/03_type_casting/3_1.py)
      - [ ] **3.2** [Convert the string "3.14" into a float and multiply it by 2.](01-fundamentals/03_type_casting/3_2.py)
      - [ ] **3.3** [Convert an int into a string and concatenate it onto another string.](01-fundamentals/03_type_casting/3_3.py)
      - [ ] **3.4** [Try converting "abc" into an int, read the error you get, and add a comment explaining what it means.](01-fundamentals/03_type_casting/3_4.py)
- [ ] **#4** ⌨️ User input
      - [ ] **4.1** [Ask for the user's name and print a greeting using it.](01-fundamentals/04_user_input/4_1.py)
      - [ ] **4.2** [Ask for two numbers with input() and print their sum (remember input() always returns a string).](01-fundamentals/04_user_input/4_2.py)
      - [ ] **4.3** [Ask for a favorite color and print it inside an f-string sentence.](01-fundamentals/04_user_input/4_3.py)
      - [ ] **4.4** [Ask for the user's birth year and calculate their approximate age.](01-fundamentals/04_user_input/4_4.py)
- [ ] **#5** 📖 [Mad Libs game](01-fundamentals/05_mad_libs_game/main.py) **⭐ mini project**
      - [ ] Ask for at least 6 different words (noun, verb, adjective, place, animal, adverb).
      - [ ] Insert them into a pre-written story of at least 4 sentences.
      - [ ] Print the final story using f-strings.
      - [ ] Bonus: let the user play again without restarting the program.

### Phase 2 — Logic & Decisions
*Teach your programs to make choices*

- [ ] **#6** 📐 Arithmetic & math
      - [ ] **6.1** [Compute and print 17 // 5 and 17 % 5 — predict both on paper before running it.](02-logic_decisions/06_arithmetic_math/6_1.py)
      - [ ] **6.2** [Compute 2 ** 10 and add a comment explaining what ** does.](02-logic_decisions/06_arithmetic_math/6_2.py)
      - [ ] **6.3** [Round 7.897 to 2 decimal places using round().](02-logic_decisions/06_arithmetic_math/6_3.py)
      - [ ] **6.4** [Compute the area of a circle given a radius, using math.pi.](02-logic_decisions/06_arithmetic_math/6_4.py)
- [ ] **#7** 🤔 If statements
      - [ ] **7.1** [Check whether a number is positive, negative, or zero.](02-logic_decisions/07_if_statements/7_1.py)
      - [ ] **7.2** [Check whether a number is even or odd using %.](02-logic_decisions/07_if_statements/7_2.py)
      - [ ] **7.3** [Check whether a given year is a leap year.](02-logic_decisions/07_if_statements/7_3.py)
      - [ ] **7.4** [Check whether three given side lengths can form a valid triangle.](02-logic_decisions/07_if_statements/7_4.py)
- [ ] **#8** 🧮 [Calculator program](02-logic_decisions/08_calculator_program/main.py) **⭐ mini project**
      - [ ] Ask for two numbers and an operator (+ - * /).
      - [ ] Support all four operators correctly.
      - [ ] Handle divide-by-zero without crashing.
      - [ ] Let the user run multiple calculations in a loop until they type 'quit'.
- [ ] **#9** 🏋️ [Weight conversion program](02-logic_decisions/09_weight_conversion_program/main.py) **⭐ mini project**
      - [ ] Ask the user which direction to convert (kg→lbs or lbs→kg).
      - [ ] Perform the correct conversion using the right formula.
      - [ ] Round the result to 2 decimal places.
      - [ ] Let them convert again without restarting the program.
- [ ] **#10** 🌡️ [Temperature conversion program](02-logic_decisions/10_temperature_conversion_program/main.py) **⭐ mini project**
      - [ ] Support Celsius→Fahrenheit, Fahrenheit→Celsius, and Celsius→Kelvin from a menu.
      - [ ] Validate the unit input and reject anything that isn't C/F/K.
      - [ ] Print the result rounded to 1 decimal place.
      - [ ] Loop until the user chooses to exit.
- [ ] **#11** 🌦️ Logical operators
      - [ ] **11.1** [Check if a number is between 1 and 100 using and.](02-logic_decisions/11_logical_operators/11_1.py)
      - [ ] **11.2** [Check if a number is NOT divisible by 3 using not.](02-logic_decisions/11_logical_operators/11_2.py)
      - [ ] **11.3** [Print "weekend" if the day is Saturday or Sunday using or.](02-logic_decisions/11_logical_operators/11_3.py)
      - [ ] **11.4** [Combine and/or to check for ("rainy" and "windy") or "snowing".](02-logic_decisions/11_logical_operators/11_4.py)
- [ ] **#12** ❓ Conditional expressions
      - [ ] **12.1** [Rewrite an if/else that prints "even"/"odd" as a one-line ternary.](02-logic_decisions/12_conditional_expressions/12_1.py)
      - [ ] **12.2** [Assign a variable status to "adult" or "minor" using a ternary expression.](02-logic_decisions/12_conditional_expressions/12_2.py)
      - [ ] **12.3** [Print "pass"/"fail" based on a score, using a ternary inside an f-string.](02-logic_decisions/12_conditional_expressions/12_3.py)

### Phase 3 — Strings
*Text manipulation - the thing you'll use constantly and never truly master*

- [ ] **#13** 〰️ String methods
      - [ ] **13.1** [Clean up "  HeLLo WoRLD  " using .strip(), .lower(), and .title().](03-strings/13_string_methods/13_1.py)
      - [ ] **13.2** [Replace all spaces in a sentence with underscores using .replace().](03-strings/13_string_methods/13_2.py)
      - [ ] **13.3** [Count how many times a letter appears in a word using .count().](03-strings/13_string_methods/13_3.py)
      - [ ] **13.4** [Split a sentence into a list of words using .split().](03-strings/13_string_methods/13_4.py)
- [ ] **#14** ✂️ String indexing & slicing
      - [ ] **14.1** [Print the first and last letter of a word.](03-strings/14_string_indexing_slicing/14_1.py)
      - [ ] **14.2** [Print a word reversed using slicing ([::-1]).](03-strings/14_string_indexing_slicing/14_2.py)
      - [ ] **14.3** [Print every other letter of a word using slicing.](03-strings/14_string_indexing_slicing/14_3.py)
      - [ ] **14.4** [Pull just the domain out of an email string using slicing/split.](03-strings/14_string_indexing_slicing/14_4.py)
- [ ] **#15** 💬 Format specifiers (f-strings)
      - [ ] **15.1** [Print a price padded to exactly 2 decimal places using an f-string.](03-strings/15_format_specifiers_f_strings/15_1.py)
      - [ ] **15.2** [Print a large number with a thousands separator (comma).](03-strings/15_format_specifiers_f_strings/15_2.py)
      - [ ] **15.3** [Pad a word to 10 characters wide, once left-aligned and once right-aligned.](03-strings/15_format_specifiers_f_strings/15_3.py)
      - [ ] **15.4** [Print a percentage using the % format spec inside an f-string.](03-strings/15_format_specifiers_f_strings/15_4.py)

### Phase 4 — Loops
*Repetition - where 'why isn't this stopping' becomes a rite of passage*

- [ ] **#16** ♾️ While loops
      - [ ] **16.1** [Keep asking for a password until it matches "python123".](04-loops/16_while_loops/16_1.py)
      - [ ] **16.2** [Count down from 10 to 1 using a while loop.](04-loops/16_while_loops/16_2.py)
      - [ ] **16.3** [Sum the numbers the user enters until they type "done".](04-loops/16_while_loops/16_3.py)
      - [ ] **16.4** [Write one while loop that uses both break and continue.](04-loops/16_while_loops/16_4.py)
- [ ] **#17** 💵 [Compound interest calculator](04-loops/17_compound_interest_calculator/main.py) **⭐ mini project**
      - [ ] Ask for principal, annual interest rate, and number of years.
      - [ ] Loop year by year, printing the running balance each year.
      - [ ] Print the total interest earned at the end.
      - [ ] Bonus: support optional monthly contributions.
- [ ] **#18** 🔁 For loops
      - [ ] **18.1** [Print the numbers 1–20, but only the odd ones.](04-loops/18_for_loops/18_1.py)
      - [ ] **18.2** [Print the multiplication table for a number the user picks.](04-loops/18_for_loops/18_2.py)
      - [ ] **18.3** [Sum all the numbers in a list using a for loop (no sum()).](04-loops/18_for_loops/18_3.py)
      - [ ] **18.4** [Loop over a string and print each character on its own numbered line.](04-loops/18_for_loops/18_4.py)
- [ ] **#19** ⌛ [Countdown timer](04-loops/19_countdown_timer/main.py) **⭐ mini project**
      - [ ] Ask the user for a number of seconds.
      - [ ] Print a countdown, one number per second, using time.sleep(1).
      - [ ] Print "liftoff!" (or similar) once it hits zero.
      - [ ] Validate that the input is a positive number.
- [ ] **#20** ➿ Nested loops
      - [ ] **20.1** [Print a 5x5 multiplication table.](04-loops/20_nested_loops/20_1.py)
      - [ ] **20.2** [Print a triangle made of stars using a nested loop.](04-loops/20_nested_loops/20_2.py)
      - [ ] **20.3** [Find all pairs (i, j) where i + j == 10 for i, j in range(1, 10).](04-loops/20_nested_loops/20_3.py)
      - [ ] **20.4** [Print a checkerboard pattern of X and O using nested loops.](04-loops/20_nested_loops/20_4.py)

### Phase 5 — Collections
*Storing more than one thing at a time, properly*

- [ ] **#21** 🍎 Lists, sets & tuples
      - [ ] **21.1** [Build a grocery list, add two items, then remove one.](05-collections/21_lists_sets_tuples/21_1.py)
      - [ ] **21.2** [Convert a list with duplicate values into a set to remove the duplicates.](05-collections/21_lists_sets_tuples/21_2.py)
      - [ ] **21.3** [Create a tuple of coordinates (x, y) and unpack it into two variables.](05-collections/21_lists_sets_tuples/21_3.py)
      - [ ] **21.4** [Sort a list of numbers in place with .sort(), then reverse it.](05-collections/21_lists_sets_tuples/21_4.py)
- [ ] **#22** 🛒 [Shopping cart program](05-collections/22_shopping_cart_program/main.py) **⭐ mini project**
      - [ ] Store cart items as a list of (name, price) tuples or dicts.
      - [ ] Let the user add items to the cart in a loop.
      - [ ] Print an itemized receipt with a running total.
      - [ ] Bonus: apply a discount if the total goes over a set threshold.
- [ ] **#23** ⬜ 2D collections
      - [ ] **23.1** [Build a 3x3 grid as a list of lists, all initialized to zero.](05-collections/23_2d_collections/23_1.py)
      - [ ] **23.2** [Print the grid row by row using nested loops.](05-collections/23_2d_collections/23_2.py)
      - [ ] **23.3** [Set a specific cell (row, col) to a value and reprint the grid.](05-collections/23_2d_collections/23_3.py)
      - [ ] **23.4** [Find the sum of every value in the grid using nested loops.](05-collections/23_2d_collections/23_4.py)
- [ ] **#24** 💯 [Quiz game](05-collections/24_quiz_game/main.py) **⭐ mini project**
      - [ ] Store at least 5 questions and answers (a list of tuples or dicts).
      - [ ] Loop through them, ask each question, and check the answer (case-insensitive).
      - [ ] Tally and print a final score out of 5.
      - [ ] Bonus: print which questions were missed at the end.
- [ ] **#25** 📙 Dictionaries
      - [ ] **25.1** [Build a dict of 3 friends → phone numbers and look one up by name.](05-collections/25_dictionaries/25_1.py)
      - [ ] **25.2** [Add a new key-value pair to an existing dict.](05-collections/25_dictionaries/25_2.py)
      - [ ] **25.3** [Loop over a dict's keys and values together using .items().](05-collections/25_dictionaries/25_3.py)
      - [ ] **25.4** [Check whether a key exists in a dict before accessing it, to avoid a KeyError.](05-collections/25_dictionaries/25_4.py)
- [ ] **#26** 🍿 [Concession stand program](05-collections/26_concession_stand_program/main.py) **⭐ mini project**
      - [ ] Store a menu as a dict of {item: price}.
      - [ ] Print the menu with prices before taking orders.
      - [ ] Let the user order multiple items by name.
      - [ ] Print an itemized total, and handle items that aren't on the menu gracefully.

### Phase 6 — Randomness & Small Games
*This is where it stops feeling like homework*

- [ ] **#27** 🎲 Random numbers
      - [ ] **27.1** [Generate a random integer between 1 and 6, like rolling a die.](06-randomness_small_games/27_random_numbers/27_1.py)
      - [ ] **27.2** [Generate a random float between 0 and 1.](06-randomness_small_games/27_random_numbers/27_2.py)
      - [ ] **27.3** [Pick a random item from a list using random.choice().](06-randomness_small_games/27_random_numbers/27_3.py)
      - [ ] **27.4** [Shuffle a list of 5 items using random.shuffle().](06-randomness_small_games/27_random_numbers/27_4.py)
- [ ] **#28** 🔢 [Number guessing game](06-randomness_small_games/28_number_guessing_game/main.py) **⭐ mini project**
      - [ ] Computer picks a random number between 1 and 100.
      - [ ] User guesses; print "higher"/"lower" hints after each guess.
      - [ ] Count and print the number of guesses it took at the end.
      - [ ] Bonus: let the user play again without restarting the program.
- [ ] **#29** 🗿 [Rock, paper, scissors](06-randomness_small_games/29_rock_paper_scissors/main.py) **⭐ mini project**
      - [ ] Computer picks randomly, user picks via input().
      - [ ] Determine and print the winner of each round.
      - [ ] Play best-of-5 and keep track of the score.
      - [ ] Handle invalid input (anything that isn't rock/paper/scissors).
- [ ] **#30** ⚂ [Dice roller program](06-randomness_small_games/30_dice_roller_program/main.py) **⭐ mini project**
      - [ ] Simulate rolling two dice N times, where N comes from user input.
      - [ ] Tally how often each total (2–12) comes up in a dict.
      - [ ] Print a simple bar chart of the results using printed asterisks.
      - [ ] Print which total came up the most.

### Phase 7 — Functions & Error Handling
*Structure your code like someone else might have to read it*

- [ ] **#31** 🧰 Functions & parameters
      - [ ] **31.1** [Write a function add(a, b) that returns their sum.](07-functions_error_handling/31_functions_parameters/31_1.py)
      - [ ] **31.2** [Write a function greet(name, greeting="Hello") that uses a default parameter.](07-functions_error_handling/31_functions_parameters/31_2.py)
      - [ ] **31.3** [Write a function that accepts *args and returns their total.](07-functions_error_handling/31_functions_parameters/31_3.py)
      - [ ] **31.4** [Turn one of your earlier scripts (e.g. temperature conversion) into a function you can call with arguments.](07-functions_error_handling/31_functions_parameters/31_4.py)
- [ ] **#32** 🏧 [ATM program](07-functions_error_handling/32_atm_program/main.py) **⭐ mini project**
      - [ ] Write deposit(), withdraw(), and check_balance() functions sharing one balance variable.
      - [ ] Build a menu loop: 1. Deposit  2. Withdraw  3. Check Balance  4. Exit.
      - [ ] Prevent overdrafts — never let the balance go negative.
      - [ ] Bonus: keep and print a transaction log at the end.
- [ ] **#33** ⚠️ Exceptions & try/except
      - [ ] **33.1** [Wrap an int() conversion of user input in try/except to catch a ValueError.](07-functions_error_handling/33_exceptions_try_except/33_1.py)
      - [ ] **33.2** [Catch a ZeroDivisionError from a division and print a friendly message instead of crashing.](07-functions_error_handling/33_exceptions_try_except/33_2.py)
      - [ ] **33.3** [Use try/except/else/finally together in one block, printing something different in each part.](07-functions_error_handling/33_exceptions_try_except/33_3.py)
      - [ ] **33.4** [Raise your own custom exception when a number is negative.](07-functions_error_handling/33_exceptions_try_except/33_4.py)
- [ ] **#34** 🛡️ [Error-proof calculator](07-functions_error_handling/34_error_proof_calculator/main.py) **⭐ mini project**
      - [ ] Rebuild exercise #8's calculator so it can never crash.
      - [ ] Handle non-numeric input, divide-by-zero, and invalid operators.
      - [ ] Wrap every risky operation in try/except.
      - [ ] Loop until the user chooses to quit, no matter what they type in the meantime.

---
*34 exercises · 7 phases · no AI allowed.*


---

## 🎁 Bonus: Mini Projects

10 extra, fun, self-contained builds outside the main curriculum — a password checker, Hangman,
a typing speed test, mini Blackjack, and more. See [`mini-projects/README.md`](mini-projects/README.md).

## 🧩 Bonus: Mini LeetCode (Easy DSA)

12 classic easy-tier algorithm problems (Two Sum, Valid Parentheses, Binary Search, ...),
each self-checking when you run the file. See [`mini-leetcode/README.md`](mini-leetcode/README.md).

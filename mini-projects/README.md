# 🎁 Mini Projects

Extra, self-contained builds — not part of the numbered curriculum, just fun stuff to build once you've got the
fundamentals down. Pick them in any order.

## Rules

- 🚫 **No AI.** No ChatGPT, no Copilot, no autocomplete you didn't type yourself.
- ✅ **Google is fine** for syntax, docs, and built-in functions.

## Projects

| # | Project | What it is |
|---|---|---|
| 1 | 🔐 [Password Strength Checker & Generator](01_password_strength_checker_generator/main.py) | Score real passwords and generate strong new ones. |
| 2 | 🤖 [Hangman](02_hangman/main.py) | The classic word-guessing game, ASCII and all. |
| 3 | ⌨️ [Typing Speed Test](03_typing_speed_test/main.py) | Time yourself retyping a sentence and get roasted by your own WPM. |
| 4 | 📓 [CLI Journal](04_cli_journal/main.py) | A tiny append-only diary that lives in a text file. |
| 5 | 🎵 [No-Repeat Playlist Shuffler](05_no_repeat_playlist_shuffler/main.py) | Shuffle a playlist so nothing repeats until everything's played. |
| 6 | 💰 [Splitwise-Lite (Bill Splitter)](06_splitwise_lite_bill_splitter/main.py) | Figure out who owes who after a group trip. |
| 7 | 🧟 [Morse Code Translator](07_morse_code_translator/main.py) | Text to dots-and-dashes and back again. |
| 8 | 🎂 [Birthday Countdown](08_birthday_countdown/main.py) | How many days until cake? |
| 9 | 🔥 [Habit Tracker with Streaks](09_habit_tracker_with_streaks/main.py) | Check off a habit each day and watch your streak grow. |
| 10 | 🃏 [Mini Blackjack](10_mini_blackjack/main.py) | You vs the dealer, one deck, no chips required. |

## Progress

- [ ] **1.** 🔐 [Password Strength Checker & Generator](01_password_strength_checker_generator/main.py)
      - [ ] Write check_strength(password) that scores it on length, upper/lowercase, digits, and symbols, returning 'weak', 'medium', or 'strong'.
      - [ ] Write generate_password(length, use_symbols=True) that returns a randomly generated strong password.
      - [ ] Build a small menu: option to check a password you type, or generate a new one.
      - [ ] Automatically mark anything under 8 characters as weak, no matter what else it contains.
- [ ] **2.** 🤖 [Hangman](02_hangman/main.py)
      - [ ] Pick a random word from a hardcoded list of at least 10 words.
      - [ ] Show blanks for unguessed letters and reveal correctly guessed ones in place.
      - [ ] Limit the player to 6 wrong guesses before they lose.
      - [ ] Print a win or lose message at the end, revealing the word either way.
- [ ] **3.** ⌨️ [Typing Speed Test](03_typing_speed_test/main.py)
      - [ ] Show the user a random sentence picked from a hardcoded list.
      - [ ] Time how long they take to retype it exactly, using the time module.
      - [ ] Calculate and print words-per-minute and character accuracy (% typed correctly).
      - [ ] Let them retry and keep track of their best WPM for the session.
- [ ] **4.** 📓 [CLI Journal](04_cli_journal/main.py)
      - [ ] Let the user write a dated journal entry from the terminal.
      - [ ] Append entries to a local text file — never overwrite previous entries.
      - [ ] Let them view all past entries, newest first.
      - [ ] Bonus: let them search past entries by keyword.
- [ ] **5.** 🎵 [No-Repeat Playlist Shuffler](05_no_repeat_playlist_shuffler/main.py)
      - [ ] Store a hardcoded playlist of at least 10 songs.
      - [ ] Shuffle it so no song repeats until every song has played once.
      - [ ] Print songs one at a time as 'Now playing', advancing with input().
      - [ ] Bonus: let the user skip a song without it counting as played.
- [ ] **6.** 💰 [Splitwise-Lite (Bill Splitter)](06_splitwise_lite_bill_splitter/main.py)
      - [ ] Let the user enter a list of people and how much each one paid.
      - [ ] Calculate each person's fair share (total ÷ number of people).
      - [ ] Print exactly who owes who, and how much, to settle up evenly.
      - [ ] Handle an uneven number of people or missing amounts gracefully.
- [ ] **7.** 🧟 [Morse Code Translator](07_morse_code_translator/main.py)
      - [ ] Build a dict mapping letters/numbers to Morse code.
      - [ ] Translate English → Morse.
      - [ ] Translate Morse → English (the reverse lookup).
      - [ ] Handle spaces between words correctly in both directions.
- [ ] **8.** 🎂 [Birthday Countdown](08_birthday_countdown/main.py)
      - [ ] Ask the user for their birthday (month and day).
      - [ ] Calculate the number of days remaining until their next birthday.
      - [ ] Handle the edge case where today IS their birthday.
      - [ ] Print a message that changes tone as it gets closer (e.g. 'so soon!' under 7 days).
- [ ] **9.** 🔥 [Habit Tracker with Streaks](09_habit_tracker_with_streaks/main.py)
      - [ ] Let the user mark a habit as 'done' for today.
      - [ ] Store completion dates in a local text file so it persists between runs.
      - [ ] Calculate their current streak (consecutive days completed).
      - [ ] Print their longest streak ever alongside their current streak.
- [ ] **10.** 🃏 [Mini Blackjack](10_mini_blackjack/main.py)
      - [ ] Build a deck and deal 2 cards each to the player and the dealer.
      - [ ] Let the player choose to hit or stand, looping until they stand or bust.
      - [ ] Implement dealer logic: dealer must hit until their hand is 17 or higher.
      - [ ] Determine and print the winner, correctly handling busts and blackjacks.

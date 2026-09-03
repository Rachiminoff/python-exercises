# 💡 Hints — 🎭 NPC Reaction Generator

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Basic ternary shape: `value = x if condition else y`.
2. Greeting: `greeting = "Welcome back." if has_met_before else "We haven't met — who are you?"`.
3. Gift reaction: `reaction = "For me? You shouldn't have." if gift_given else "Empty-handed, huh?"`.
4. Nested ternary for three moods:
   `mood_line = "😊 Great to see you!" if mood == "friendly" else ("😐 Oh. It's you." if mood == "neutral" else "😠 Get out of my sight.")`.
5. The "only ternaries in main()" constraint is the real exercise — if you reach for `if x:` on its own
   line, that's the cue to fold it into an expression instead.
6. f-strings combine all three lines into one block: `print(f"{greeting}\\n{reaction}\\n{mood_line}")`.

## Relevant functions & syntax

`x if condition else y`, nested ternaries, f-strings

[← back to mini-projects](README.md)

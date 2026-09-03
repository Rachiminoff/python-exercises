# 💡 Hints — 🕵️ Secret Agent Access Control

Try the exercise for real first. These are ordered from vague to specific — stop reading as soon as you
see a way forward.

## Hints

1. Turn yes/no input into real booleans once, up front:
   `has_keycard = input("Do you have a keycard? (yes/no): ").lower() == "yes"`.
2. Write each room's rule as its own boolean variable before printing anything — it's much easier to
   debug `vault_access = has_keycard and (clearance or escorted) and not alarm_active` on its own line
   than buried inside an `if`.
3. To report *why* access was denied, check the failing piece separately, e.g.
   `if not has_keycard: print("Missing keycard")`. You can do this after already knowing the room failed.
4. Store rooms as a list of (name, boolean_result) pairs so you can loop through and print each one instead
   of repeating the same print logic three times.

## Relevant functions & syntax

boolean conversion from input, `and`, `or`, `not`, tuples/lists for grouping results

[← back to mini-projects](README.md)

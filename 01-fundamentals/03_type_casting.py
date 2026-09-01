"""
Exercise #3: Type casting 💱
Phase 1: Fundamentals

Task:
    Take a number typed as a string and convert it to an int and a float. Try breaking it on purpose with letters.

Rules:
    - No AI — no Copilot / ChatGPT / autocomplete you didn't type yourself.
    - Google is fine for syntax, docs, and built-in functions.
"""

# TODO: write your solution below


def main():
    numberStr = "19"
    anotherStr = "8.43"
    
    
    integer = int(numberStr)
    floatVal = float(anotherStr)
    
    print(integer)
    print(floatVal)
    
    result = integer + floatVal
    print(result)


if __name__ == "__main__":
    main()

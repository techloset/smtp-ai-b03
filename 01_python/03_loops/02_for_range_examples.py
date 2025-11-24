"""for loop with range()

range() is used to generate a sequence of numbers.
We often use it when we know how many times we want to repeat something.

Examples:
- Print even numbers from 0 to 10
- Countdown timer
"""

print("Even numbers from 0 to 10:")

for number in range(0, 11, 2):
    print(number)

print("--------------------------------")

print("Countdown from 5 to 1:")

for number in range(5, 0, -1):
    print(number)

print("Blast off!")



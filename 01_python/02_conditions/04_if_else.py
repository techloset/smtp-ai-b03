"""if / else: choose between two paths

We use if/else when we want to do ONE thing if a condition is True,
and a DIFFERENT thing if it is False.
Example:
- "If score >= 50: Pass, else: Fail"
"""

score = 72

print("Score:", score)

if score >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

print("--------------------------------")

# Real-world style example: even or odd number checker
number = 9

print("Number:", number)

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

print("Check complete.")



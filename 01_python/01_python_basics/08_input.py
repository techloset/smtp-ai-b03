# We take input from users to make programs interactive, like forms, quizzes, and calculators.
# Getting input from the user.

name = input("Enter your name: ")
age_text = input("Enter your age: ")

# Convert the age from text to number
age = int(age_text)

print(f"Hello {name}, next year you will be {age + 1} years old.")

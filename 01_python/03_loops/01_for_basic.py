"""Basic for loop

We use for loops to repeat an action a fixed number of times or
for each item in a collection.

Examples:
- Send a notification to each user
- Print numbers from 1 to 10
"""

print("Counting from 1 to 5:")

for number in range(1, 6):
    print("Number:", number)

print("--------------------------------")

names = ["Ali", "Sara", "Danish"]

print("Greeting each name in a list:")

for name in names:
    print("Hello,", name)

print("Loop finished.")


# Practice Examples (add your solutions below):
# 1. Print all even numbers from 1 to 20
# 2. Calculate sum of all numbers from 1 to 50
# 3. Print each character of your name with its position (use a counter)
# 4. Ask user for a number and print its multiplication table (1 to 10)
# 5. Count how many vowels are in the word "programming"

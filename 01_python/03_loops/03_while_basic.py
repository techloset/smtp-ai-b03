"""Basic while loop

We use while loops to repeat an action WHILE a condition is True.
Be careful to update the condition, otherwise you get an infinite loop.

Examples:
- Ask for a password until it is correct
- Count up until a limit
"""

print("Counting up with while loop:")

count = 1
while count <= 5:
    print("Count =", count)
    count = count + 1  # update the variable so the loop can stop

print("--------------------------------")

print("Simple login attempt example:")

correct_password = "python123"
password = input("Enter password: ")

while password != correct_password:
    print("Wrong password. Try again.")
    password = input("Enter password: ")

print("Login successful!")


# Practice Examples (add your solutions below):
# 1. Keep doubling a number starting from 1 until it exceeds 1000
# 2. Ask user for a positive number, keep asking until they enter one
# 3. Calculate factorial of a number using while loop
# 4. Keep asking for password (max 3 attempts) using a counter
# 5. Find the first number divisible by 7 and 13 between 1-500

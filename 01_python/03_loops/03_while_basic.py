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



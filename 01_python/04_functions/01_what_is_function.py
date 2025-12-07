# ============================================
# LESSON 1: What is a Function?
# ============================================

# A function is a REUSABLE block of code that does a specific task
# Think of it like a recipe - you write it once, use it many times!

# WHY use functions?
# 1. Avoid repeating code
# 2. Make code easier to read
# 3. Break big problems into small pieces


# ============================================
# Creating Your First Function
# ============================================

# To create a function, use the 'def' keyword
# Syntax:
#   def function_name():
#       code goes here

def say_hello():
    print("Hello, World!")


# ============================================
# Calling (Using) a Function
# ============================================

# Creating a function doesn't run it!
# You need to CALL it by using its name with parentheses ()

print("Let's call our function:")
say_hello()  # This runs the function

print("\nWe can call it again:")
say_hello()  # Run it again - reusable!

print("\nAnd again:")
say_hello()  # See? We wrote it once, use many times!


# ============================================
# More Simple Function Examples
# ============================================

def print_line():
    """Prints a decorative line"""
    print("=" * 30)


def greet_user():
    """Prints a friendly greeting"""
    print("Welcome to Python!")
    print("Let's learn functions together!")


def show_menu():
    """Prints a simple menu"""
    print("1. Start")
    print("2. Settings")
    print("3. Exit")


# Let's use our functions!
print("\n--- Using print_line function ---")
print_line()

print("\n--- Using greet_user function ---")
greet_user()

print("\n--- Using show_menu function ---")
print_line()
show_menu()
print_line()

# ============================================
# EXERCISE: Try it yourself!
# ============================================

# Create a function called 'introduce_yourself' that prints:
# - Your name
# - Your favorite hobby
# Then call it!

# Write your code below:
# def introduce_yourself():
#     print("My name is ...")
#     print("My hobby is ...")
#
# introduce_yourself()



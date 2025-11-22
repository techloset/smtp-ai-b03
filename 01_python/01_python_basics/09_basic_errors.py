# Examples of common syntax errors and runtime errors.


print("This file shows examples of common Python errors.")

# ----------------------
# Syntax error examples
# ----------------------

# 1) Missing closing parenthesis
# print("Hello, World!"   # SyntaxError: '(' was never closed

# 2) Wrong indentation
#   print("Bad indent")   # IndentationError

# ----------------------
# Runtime error examples
# ----------------------

# 3) ZeroDivisionError
# result = 10 / 0
# print(result)

# 4) TypeError - mixing incompatible types
# total = 10 + "10"
# print(total)

# 5) ValueError - invalid conversion
# number = int("10a")
# print(number)

print("Run this file, then uncomment one error example to see what happens.")

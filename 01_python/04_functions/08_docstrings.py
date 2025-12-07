# LESSON 8: Docstrings
# Document what your function does

# === Single-Line Docstring ===
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# === Multi-Line Docstring ===
def calculate_bmi(weight, height):
    """
    Calculates Body Mass Index.
    
    Parameters:
        weight: Weight in kg
        height: Height in meters
    
    Returns:
        float: BMI value
    """
    return weight / (height ** 2)

# === Accessing Docstrings ===
print(add.__doc__)
print()
help(calculate_bmi)

# === Practical Example ===
def validate_password(password, min_length=8):
    """
    Validates password strength.
    
    Parameters:
        password: Password to check
        min_length: Minimum length (default: 8)
    
    Returns:
        tuple: (is_valid, message)
    """
    if len(password) < min_length:
        return False, "Too short"
    if not any(c.isdigit() for c in password):
        return False, "Need a digit"
    return True, "Valid"

print(validate_password("abc"))
print(validate_password("password1"))

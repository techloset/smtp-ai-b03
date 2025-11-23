"""if / elif / else: multiple choices

We use if/elif/else to pick ONE matching option from several.
Real-life examples:
- Assigning a grade (A, B, C, D, F)
- Choosing a ticket price based on age groups
"""

score = 83

print("Score:", score)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print("--------------------------------")

# Real-world style example: cinema ticket price based on age
age = 10

print("Age:", age)

if age < 12:
    price = 5  # child price
elif age <= 60:
    price = 10  # standard adult price
else:
    price = 7  # senior price

print("Ticket price:", price, "USD")



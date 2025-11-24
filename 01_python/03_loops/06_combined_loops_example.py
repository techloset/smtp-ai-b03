"""Combined loops – realistic scenario

This file puts together:
- for loops
- while loops
- range()
- break and continue

Scenario: simple shopping cart summary
"""

print("Shopping cart example:")

cart_items = ["Apple", "Banana", "Orange", "Stop", "Mango"]

print("Items in cart (we stop at 'Stop'):")

for item in cart_items:
    if item == "Stop":
        print("Reached 'Stop' marker. Ending list.")
        break
    print("-", item)

print("--------------------------------")

print("Total price calculator (while loop):")

total = 0

while True:
    price_text = input("Enter item price (or '0' to finish): ")
    price = float(price_text)

    if price == 0:
        break  # stop when user enters 0

    if price < 0:
        print("Negative price is not allowed. Try again.")
        continue  # skip adding negative values

    total = total + price
    print("Current total:", total)

print("Final total to pay:", total)



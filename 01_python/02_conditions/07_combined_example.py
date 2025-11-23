"""Combined conditions – realistic scenario

This file puts together:
- comparison operators
- logical operators
- if / elif / else

Scenario: online order rules
- Free shipping if total >= 50 OR user is premium
- Extra discount if it is a weekend AND total >= 100
- Otherwise, show normal message
"""

order_total = 85
is_premium_member = False
is_weekend = True

print("Order total:", order_total)
print("Is premium member:", is_premium_member)
print("Is weekend:", is_weekend)
print("--------------------------------")

# Free shipping rule
if order_total >= 50 or is_premium_member:
    print("✅ You get free shipping!")
else:
    print("🚚 Shipping will be added to your order.")

# Extra discount rule
if is_weekend and order_total >= 100:
    print("🎉 Weekend sale: extra 10% discount applied!")
elif is_weekend:
    print("🎉 Weekend sale is on! Add more items to reach 100 for extra discount.")
else:
    print("No extra weekend discount today.")

print("Thank you for shopping with us.")



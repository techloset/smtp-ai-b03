# Converting between different data types.

# String to integer
age_text = "21"
age_number = int(age_text)  # convert string to int

print("Age as text:", age_text, type(age_text))
print("Age as number:", age_number, type(age_number))

# Integer to string
year = 2025
year_text = str(year)
print("Year as text:", year_text, type(year_text))

# Float from input-like value
price_text = "19.99"
price = float(price_text)
print("Price:", price, type(price))


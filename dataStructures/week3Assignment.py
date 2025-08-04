# # week assignment 
# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount = (discount_percentage / 100) * price
        final_price = price - discount
        return final_price
    else:
        return price

# promptint the user
price = float(input("enter the price of the last pair of shoes you bought \n"))
discount_percentage = float(input("enter the discount you were offered (dont include percentage)"))

print(calculate_discount(price, discount_percentage))

# task2_discount.py

# 1. Get the input
bill_amount = input("Enter your total bill amount: ")

# 2. Convert to a number (float is good for money!)
bill_amount = float(bill_amount)

# 3. Apply discounts using if/elif/else
if bill_amount >= 5000:
    discount = bill_amount * 0.20
    final_price = bill_amount - discount
    print("You get a 20% discount!")
    print("Discount amount: ₹", discount)
    print("Your final bill is: ₹", final_price)

elif bill_amount >= 2000:
    discount = bill_amount * 0.10
    final_price = bill_amount - discount
    print("You get a 10% discount!")
    print("Discount amount: ₹", discount)
    print("Your final bill is: ₹", final_price)

else:
    print("No discount applied.")
    print("Your final bill is: ₹", bill_amount)
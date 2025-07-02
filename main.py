print("Welcome to the Tip Calculator")
order_total = float(input("What's the total amount of your order? $"))
tip_percent = float(input("What percent do you want to tip? ")) / 100

tip_amount = order_total * tip_percent
final_order_total = order_total + tip_amount

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount to pay: ${final_order_total:.2f}")

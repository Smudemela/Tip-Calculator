print("Welcome to the Tip Calculator")
order_total = float(input("What's the total amount of your order? "))
tip_percent = float(input("What percent do want to tip?"))

tip_amount = float(order_total*tip_percent)
final_order_total = order_total+tip_amount

print(tip_amount)
print(final_order_total)

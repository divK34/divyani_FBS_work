# WAP to calculate selling price of book based on cost price and discount.
# selling price (SP) = cost price (CP) - discount

cost_price = int(input("Enter cost price: "))
discount = int(input("Enter discount: "))

discounted_price = cost_price * (discount / 100)
selling_price = cost_price - discounted_price

print("Selling price =",selling_price)

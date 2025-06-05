# Write a program to calculate profit or loss
# Cost Price = the price at which goods are bought from merchant or retailer
# Selling Price = the price that customers pays to purchase a product
# profit = Selling Price (S.P.) - Cost Price (C.P.)
# loss = Cost Price - Selling Price

cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))

profit = sp - cp

if profit > 0:
    print("It is Profitable by ", profit)
else:
    print("It is in Loss by ", profit)
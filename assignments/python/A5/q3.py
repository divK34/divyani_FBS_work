# Accept no. of passengers from user and per ticket cost. 
# Then accept age of each passenger and 
# then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full

num = int(input("Enter total number of passengers: "))
total_cost = 0

i = 0
while i != num:
    per_tic_cost = int(input("Enter ticket cost: "))
    age = int(input("Enter age: "))

    if age < 12:
        discount = per_tic_cost * 0.30
        total_cost = total_cost + (per_tic_cost - discount)
    elif age > 59:
        discount = per_tic_cost * 0.50
        total_cost = total_cost + (per_tic_cost - discount)
    else:
        total_cost = total_cost + per_tic_cost

    i += 1

print("Total cost of",num,"passengers is = ",total_cost)            


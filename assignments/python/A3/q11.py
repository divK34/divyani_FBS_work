# Accept age of five people and also per person ticket amount and 
# then calculate total amount to ticket to travel for all of them based on following condition :
# a.Children below 12 = 30% discount
# b.Senior citizen (above 59) = 50% discount
# c.Others need to pay full

total_amt = 0

for i in range(5):
    age = int(input("Enter age: "))
    ticket_amt = int(input("Enter ticket amt: "))

    if age < 12:
        discount = ticket_amt * (30 / 100)
        ticket_amt = ticket_amt - discount
    elif age >= 59:
        discount = ticket_amt * (50 / 100)
        ticket_amt = ticket_amt - discount
    else:
        pass

    total_amt += ticket_amt    

print("Total amount of tickets is =",total_amt)    


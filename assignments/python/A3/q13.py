# Write a program to input electricity unit charges and 
# calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

elec_units = int(input("Enter the electricity units : "))
tot_bill = 0

if elec_units <= 50:
    tot_bill = elec_units * 0.5
    print("Total Bill is :",tot_bill)

elif elec_units <= 150 and elec_units > 50:
    tot_bill = (50 * 0.5) + ((elec_units - 50) * 0.75)
    print("Total Bill is :",tot_bill)

elif elec_units <= 250 and elec_units > 150:
    tot_bill = (50 * 0.5) + (100 * 0.75) + ((elec_units - 150) * 1.2)
    print("Total Bill is :",tot_bill)

else:
    tot_bill = (50 * 0.5) + (100 * 0.75) + (100 * 1.2) + ((elec_units - 250) * 1.5)
    print("Total Bill is :",tot_bill)
    print('Process Completed')
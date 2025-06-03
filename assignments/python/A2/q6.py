# WAP to calculate total salary (gross salary) of employee based on basic, 
# Formula := Basic salary = Gross salary - (da + ta + hra)
# Dearness Allowance (DA) = 10% of basic, 
# Travel Allowance (TA) = 12% of basic, 
# House Rent Allowance (HRA) = 15% of basic. 

basic_salary = int(input("Enter basic salary amount : "))

da = basic_salary * (10 / 100)
ta = basic_salary * (12 / 100)
hra = basic_salary * (15 / 100)

total_salary = basic_salary + da + ta + hra
print("Gross Salary = ", total_salary)
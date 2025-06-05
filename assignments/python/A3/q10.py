# WAP to check if person is eligible to marry or not (male age >=21 and female age>=18)

age = int(input("Enter age: "))
gender = input("Enter gender, f or m: ")

if (age >= 18) and (gender == "f"):
    print("Eligible for marriage")
elif (age >= 21) and (gender == "m"):
    print("Eligible for marriage")
else:
    print("Not eligible for marriage")

# 7. WAP to check if user has entered correct userid and password
# 8. WAP to prompt user to enter userid and password.
# After verifying userid and password display a 4 digit random number and ask user to enter the same.
# If user enters the same number then show him success message otherwise failed. (Something like captcha)

first_name = input("Enter first name : ")
last_name = input("Enter last name: ")

user_id = input("Enter user id with gmail: ")
password = int(input("Enter password with integers: "))

if (first_name in user_id) and (last_name in user_id) and ("@gmail.com" in user_id):
    print("User_id is correct")
else:
    print("User_id is not correct")

if type(password) == int:
    print("Password is correct")    
else:
    print("Password is not correct")

random_num = 8576
print(random_num)

user_num = int(input("Enter the 4 digit number: "))

if user_num == random_num:
    print("Verification Successful!")
else:
    print("Verification Unsuccessful.")

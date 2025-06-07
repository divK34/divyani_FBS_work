# Write a program to prompt user to enter userid and password.
# If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times.
# After that program to terminate.

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
userid = input("Enter userid: ")
password = input("Enter password: ")

i = 0
while i < 4:
    if ((first_name not in userid) or (last_name not in userid)) and ((type(password) == int) and (len(password) == 8)) : 
        print("userid invalid please try again")
        userid = input("Enter userid: ")
        password = int(input("Enter password: "))
        i += 1
    else:
        print("Welcome aboard!!")
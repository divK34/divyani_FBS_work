# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
maths = int(input("Enter your maths marks out of 100: "))
science = int(input("Enter your science marks out of 100: "))
english = int(input("Enter your english marks out of 100: "))
history = int(input("Enter your history marks out 100: "))
marathi = int(input("Enter your marathi marks out 100: "))

total_marks = ((maths + science + english + history + marathi) / 500) * 100

if total_marks >= 60:
    print("First Class")
elif (total_marks >= 50) and (total_marks < 60):
    print("Second Class")
elif (total_marks >= 30) and (total_marks < 50):
    print("Pass")
else:
    print("Fail")

# Enter number of students from user.
# For those many students accept marks of 5 subject marks from user and calculate percentage. 
# Display all percentage and average percentage of students.

num = int(input("Enter total number of students: "))
sum_of_percents = 0
i = 0
while i != num:
    maths = int(input("Enter the maths marks out of 100: "))
    science = int(input("Enter the science marks out of 100: "))
    history = int(input("Enter the history marks out of 100: "))
    english = int(input("Enter the english marks out of 100: "))
    geography = int(input("Enter the geography marks out of 100: "))

    percentage = ((maths + science + history + english + geography) / 500) * 100
    sum_of_percents = sum_of_percents + (percentage / 100)    
    print(i,". Percentage of student: ",percentage)
    i += 1

avg_of_all_percents = (sum_of_percents / num) * 100
print("Class percentange : ", avg_of_all_percents)    
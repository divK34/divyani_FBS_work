# Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set. 

set1 = {10, -5, 3, 7, -2}
set2 = {4, -8, 0, 15, -1}

print(f"The difference between {set1} and {set2} = {set1.difference(set2)}")
print(f"The difference between {set2} and {set1} = {set2.difference(set1)}")
print(f"The symmetric difference between {set1} and {set2} = {set1.symmetric_difference(set2)}")

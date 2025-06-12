# WAP to find maximum and minimum element in the list.

l1 = [22, 45, 67, 34, 99, 100, 345, 334]
max = l1[0]
min = l1[0]

for ele in l1:
    if ele > max :
        max = ele
    elif ele < min:
        min = ele
        
print("Maximum = ",max)
print("Minimum = ",min)
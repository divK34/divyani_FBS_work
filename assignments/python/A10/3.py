# WAP to find second largest element in list

l1 = [98, 100, 500, 99, 20, 45, 69, 98]

max1 = l1[0]
max2 = 0

for ele in l1:
    if ele > max1:
        max1 = ele
        max2 = max1
    elif ele < max1 and ele != max2:
        max2 = ele

print("The second largest element is =", max2)
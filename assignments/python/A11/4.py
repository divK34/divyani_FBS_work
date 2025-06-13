# Python Program to Find the Second Largest Number in a List Using Bubble Sort 

l1 = [12,24,36,32,14,26,99,35,89,31]

for i in range(0,len(l1)):
    for j in range(i+1, len(l1)):
        if l1[j] < l1[i]:
            l1[j], l1[i] = l1[i], l1[j]

print("Second largest = ",l1[-2])
# WAP to remove all occurrences of a given element in the list.

l1 = [23,45,67,89,12,45,56,67,56,56,89,90,22]
print(l1)
n = int(input("Enter an element to remove from list: "))

for i in range(len(l1)-1,-1,-1):
    if n == l1[i]:
        l1.pop(i)

print(l1)
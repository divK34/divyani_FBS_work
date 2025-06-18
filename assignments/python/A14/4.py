# Python Program that finds all pairs of element in a list whose sum is equals to a given value.

n = int(input("Enter a number: "))
list1 = [13,66,73,9,14,27,5,4,35]
print(list1)
list2 = []
for i in range(len(list1)):
    for j in range(len(list1)-1,0,-1):
        if n in list1:
            list2.append(n)
        elif n == (list1[i] + list1[j]):
            list2.append(list1[i])
            list2.append(list1[j])
        else:
            continue
        
set1 = set(list2)
print(set1)
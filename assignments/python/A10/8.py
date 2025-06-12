# WAP to create a duplicate of an existing list. It should not point to same list

l1 = [23,34,45,56,23,34]

l2 = []

for ele in l1:
    l2.append(ele)

print(l2)
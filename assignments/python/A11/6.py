# Python Program to Find the Union of two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("List 1 =", list1)
print("List 2 =", list2)

lists_union = list(set(list1) | set(list2))

print("Union of the two lists =", lists_union)

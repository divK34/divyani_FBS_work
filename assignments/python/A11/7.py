# Python Program to Find the Intersection of Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("List 1 =", list1)
print("List 2 =", list2)

lists_intersection = list(set(list1) & set(list2))

print("Intersection of the two lists =", lists_intersection)

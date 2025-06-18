# Python program to find elements in a given set that are not in another set.

set1 = {12,45,78,98,54}
set2 = {"a",44,"g",12,45,78}
print("set 1 =",set1)
print("set 2 =",set2)
res = set1.difference(set2)
print("elements in set one that are not in set two = ",res)
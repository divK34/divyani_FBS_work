# WAP to find sum of all elements in list

from functools import reduce

l1 = [10, 20, 30, 40, 50]
add = lambda x, y: x + y
res = reduce(add, l1)
print("Sum of all elements =",res)
# Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

l1 = [23, 34, 45, 56, 67, 78, 89, 34, 90, 45]
l1 = list(set(l1))
l1.sort()

lp = l1[-1] * l1[-2]
sp = l1[0] * l1[1]

if lp > sp:
    print([l1[-2], l1[-1]])
else:
    print([l1[0], l1[1]])
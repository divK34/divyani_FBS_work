# Python Program to Sort a List According to the Length of the Elements within the list.

l1 = [[1,2,3],[1,2,3,4],[1,2],[1]]

l1.sort(key=len)
print("Sorted by length =", l1)
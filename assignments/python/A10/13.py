# Write a program to print list after removing even numbers.

l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1)
for ele in l1:
    if ele % 2 == 0:
        l1.remove(ele)

print("only odd ones =",l1)
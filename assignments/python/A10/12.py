#  Write a program to create three lists of numbers, their squares and cubes

l1 = [1,2,3,4,5,6,7,8,9,10]

sqs = []
cubes = []

for ele in l1:
    sqs.append(ele ** 2)
    cubes.append(ele ** 3)

print(l1)
print(sqs)
print(cubes)
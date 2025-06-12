# WAP to create a new list from existing list which contains cube of each number of list.

l1 = [1,2,3,4,5,6,7,8,9,10]
cube_l1 = []

cube = lambda x : x ** 3
res = map(cube, l1)

for ele in res:
    cube_l1.append(ele)

print(l1)
print(cube_l1)
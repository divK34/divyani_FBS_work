# 1
# 1 2       
# 1   3
# 1     4
# 1 2 3 4 5

n = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or i == j or i == n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

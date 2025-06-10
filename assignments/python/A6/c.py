#    1 
#   1 1 
#  1 2 1 
# 1 3 3 1 

n = 4

for i in range(n):
    for j in range((n-1)-i):
        print(" ",end="")
        
    for j in range(i+1):
        if (j == 0) or (j == i):
            print(1,end=" ")
        else:
            print(i,end=" ")
    print()
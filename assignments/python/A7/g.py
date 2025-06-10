#         1 
#       1 2 1 
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

n = 5

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    
    for j in range(1,i+1):
        print(j,end=" ")
    
    x = i 
    x -= 1
    for j in range(2,i+1):
        print(x, end=" ")
        x -= 1   
    print()

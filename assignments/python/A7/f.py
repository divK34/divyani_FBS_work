# 1 2 3 4 5       
# 2     5 
# 3   5   
# 4 5     
# 5    

n = 5

for i in range(1, n+1):
    
    for j in range(1, n+1):
        if j == 1:
            print(i, end=" ")
    
    for j in range(2, n+1):
        if i == 1:
            print(j, end=" ")
    
    for j in range(n-1,1,-1):
        if j == i:
            print(n, end=" ")
        else:
            print(" ", end=" ")
    
    print()
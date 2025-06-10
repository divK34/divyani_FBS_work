#         1 
#       1 2 3       
#     1 2 3 4 5     
#   1 2 3 4 5 6 7   
# 1 2 3 4 5 6 7 8 9 

n = 5
for i in range(1,n+1):
    for j in range(i,n+1):      # space block
        print(" ",end=" ")
    
    x = 1
    for j in range(1,i+1):      # right-side aligned triangle         
        print(x,end=" ")
        x += 1
    
    for j in range(1,i):      # left-side aligned triangle
        print(x,end=" ")
        x += 1
    print()
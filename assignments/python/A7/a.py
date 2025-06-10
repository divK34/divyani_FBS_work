#     *    
#    * *   
#   *   *  
#  *     * 
# *       *
# *       *
#  *     * 
#   *   *  
#    * *   
#     *  

n = 5

for i in range(1,n+1):
    for j in range(1,n+1):
        if j + i == (n + 1):
            print("*",end="")
        else:
            print(" ",end="")

    for j in range(2,n+1):
        if i == j:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(1,n+1):    
    for j in range(1,n+1):
        if j == i:
            print("*",end="")
        else:
            print(" ",end="")
    
    for j in range(1,n):
        if j + i == n:
            print("*",end="")
        else:
            print(" ",end="")
    
    print()
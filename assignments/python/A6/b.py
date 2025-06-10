# 1 
# 2 3      
# 4 5 6    
# 7 8 9 10 

n = 5
x = 1
for i in range(1,n):    
    for j in range(i):
        print(x,end=" ")
        x += 1
    print()
#           A 
#         A B C 
#       A B C D E 
#     A B C D E F G 
#   A B C D E F G H I

n = 5
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end=" ")
    
    x = 0
    for j in range(i):
        print(chr(ord("A") + x),end=" ")
        x += 1
    
    for j in range(1,i):
        print(chr(ord("A") + x),end=" ")
        x += 1
    print()
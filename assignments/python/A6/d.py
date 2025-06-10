# A 
# A B 
# A B C
# A B C D
# A B C D E

n = 5
for i in range(1,n+1):
    x = 0
    for j in range(i):
        print(chr(ord("A") + x),end=" ")
        x += 1
    print()
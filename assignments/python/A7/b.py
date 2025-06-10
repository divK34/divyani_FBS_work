# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 5
for i in range(1,n+1):
    for j in range(n):
        if j < i:
            print("*",end=" ")
    print()

for i in range(1,n):
    for j in range(1,n):
        if i <= j:
            print("*",end=" ")
    print()
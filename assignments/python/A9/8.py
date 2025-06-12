# Write a program to check whether a number is prime or not using recursion

def pon(n, i):
    if i < n:
        if n % i == 0:
            return False
        return pon(n, i+1)
    else:
        return True


n = int(input("Enter a number: "))
i = 2
flag = pon(n, i)
if flag == True:
    print(n,"is a Prime Number.")        
else:
    print(n,"is not a Prime Number.")
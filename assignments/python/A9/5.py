# Write a program to find factorial using recursion.

def factorial(i, num, fact):
    if i <= num:
        fact *= i
        return factorial(i+1, num, fact)
    else:
        return fact


num = int(input("Enter a number to check its factorial: "))
i = 1
fact = 1
res = factorial(i, num, fact)
print("Factorial of",num,"=",res)
# Write a program to find sum of digits using recursion.

def sod(n, sum):
    if n != 0:
        rem = n % 10
        sum += rem
        return sod(n // 10, sum)
    else:
        return sum

n = int(input("Enter a number: "))
sum = 0
res = sod(n, sum)
print("sum of digits of number",n,"=",res)
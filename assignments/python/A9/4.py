# Write a program to find sum of n numbers using recursion.


def son(n, i, sum):
    if i <= n:
        sum += i
        return son(n, i+1, sum)
    else:
        return sum


n = int(input("Enter a number: "))
i = 1
sum = 0
res = son(n, i, sum)
print(res)
# Write a program to print Fibonacci series using recursion.
# 0 1 1 2 3 5 8 13 21 34 55 89

def fibo(i, n, f0, f1):
    if i <= n:
        fn = f0 + f1
        print(fn, end=" ")
        fibo(i+1, n, f1, fn)
     

n = int(input("Enter a number: "))
f0 = 0
f1 = 1
print(f0, f1, end=" ")
i = 1
fibo(i, n, f0, f1)



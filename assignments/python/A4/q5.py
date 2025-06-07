# WAP to print Fibonacci series upto n.
# 0 1 1 2 3 5 8 so on..

term = int(input("Enter a number for range: ")) 

first = 0
second = 1
third = 0

for i in range(term):
    print(first, end=" ")
    third = first + second
    first = second
    second = third
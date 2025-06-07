# WAP to check if a given number is prime number or not.
# all numbers, that are only divisible by 1 and itself. 
# logic = if n is not divisible by 2 to n-1 then it is a prime number

n = int(input("Enter a number: "))
# flag = True                            # note:  0 is false and 1 is true

for i in range(2, n):
    if n % i == 0:
        print(n,": is not a Prime number")
        break
else:
    print(n,": is a Prime number")
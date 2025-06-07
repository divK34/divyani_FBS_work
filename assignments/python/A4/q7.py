# WAP to print all integers upto n that aren’t divisible by 2 and 3. 

n = int(input("Enter a number: "))

for i in range(n):
    if i % 2 != 0 and i % 3 != 0:
        print(i,": is not divisible by 2 and 3.")
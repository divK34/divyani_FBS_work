# WAP to print first n prime number

n = int(input("Enter a number: "))

cnt = 0
num = 2
while cnt != n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ") 
        cnt += 1
    num += 1



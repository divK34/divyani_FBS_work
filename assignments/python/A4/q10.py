# WAP to check if given number is Perfect Number.
# perfect number =  sum of factors of the number are equal to the number 

n = int(input("Enter a number: "))
sum_of_factors = 0

for i in range(1, n):              
    if n % i == 0:                  
        sum_of_factors += i
        # print(i, "is a factor of", n)   

if sum_of_factors == n:
    print(n, "is a Perfect Number")
else:
    print(n, "is not a Perfect Number")                    


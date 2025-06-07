# WAP to print sum of series upto n. 

n = int(input("Enter a number: "))
sum_res = 0

for i in range(1, n + 1):
    sum_res += i

print("Sum of series upto number",n,"=",sum_res)
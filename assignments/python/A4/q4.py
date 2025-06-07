# WAP to print factorial of a number.
# 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040

num = int(input("Enter a number that you want fatorial of: "))
res = num 
for i in range(1, num):
    res *= i                

print("Fatorial of",num,"is",res)
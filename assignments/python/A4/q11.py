# strong number : sum of the factorial of each number is eactly equal to the given number

num = int(input("Enter a number: "))
quo = num
sum = 0

while quo != 0:
    rem = quo % 10
    quo = quo // 10
    
    fact = 1
    for i in range(2, rem+1):
        fact *= i
    
    sum = sum + fact            # 120 # 144 # 145

if sum == num :
    print(num,": is a Strong number")
else:
    print(num, ": is not a Strong number")
   
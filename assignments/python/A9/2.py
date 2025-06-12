# Write a program to check if given number is Armstrong or not using recursive function.
# 1**3 + 5**3 + 3**3 = 1+125+27 = 153

def armstrong_or_not(num, num_len, sum):
    if num != 0:
        rem = num % 10
        sum += rem ** num_len
        return armstrong_or_not(num // 10, num_len, sum)
    else:
        return sum

num = int(input("Enter a number:"))
num_len = len(str(num))
sum = 0
res = armstrong_or_not(num, num_len, sum)
if res == num:
    print(num,"is an Armstrong Number.")
else:
    print(num,"is not an Armstrong Number.")
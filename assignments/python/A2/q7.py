# Find the sum of three-digit number.

num = int(input("Enter three-digit number: "))

rem1 = num % 10     # 143 % 10 = 3
quo1 = num // 10    # 143 // 10 = 14
rem2 = quo1 % 10    # 14 % 10 = 4
quo2 = quo1 // 10   # 14 // 10 = 1

sum_of_num = rem1 + rem2 + quo2
print("Sum of", num, "=", sum_of_num)

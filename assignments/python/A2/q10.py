# WAP to reverse three-digit number.

num = int(input("Enter a three-digit number: "))

third = num % 10     # 153 % 10 = 3
quo1 = num // 10    # 153 // 10 = 15
second = quo1 % 10    # 15 % 10 = 5
first = quo1 // 10   # 15 // 10 = 1

reversed = (third * 100) + (second * 10) + first
print("Reversed =",reversed)
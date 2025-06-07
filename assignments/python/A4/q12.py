# WAP to print Armstrong number within a given range
# sum of numbers, each power to the total number of the digits in that number 
# ex := 153 = 1 ** 3 + 5 ** 3 + 3 ** 3 = 1 + 125 + 27 = 153

r = input("Enter range for armstrong number: ")
print("Armstrong number winthin range",r,"are :")
for num in range(1, int(r)):
    size_of_num = len(str(num))
    
    quo = int(num)
    sum = 0
    while quo != 0:
        rem = quo % 10      
        quo = quo // 10        
        sum = sum + (rem ** size_of_num)
    
    if sum == num:
        print(num)
        
# WAP to check if given number is Armstrong number or not.
# (Hint: 153=1*1*1+5*5*5+3*3*3,1634=1*1*1*1+6*6*6*6+3*3*3*3+ 4*4*4*4)

for num in range(1, 100):
    size_of_num = len(str(num))
    
    quo = int(num)
    sum = 0
    while quo != 0:
        rem = quo % 10      
        quo = quo // 10        
        sum = sum + (rem ** size_of_num)
    
    if sum == num:
        print(num) 

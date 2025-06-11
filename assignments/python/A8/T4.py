# Type 4 - with parameter, with return type.

# 1. Write a program to calculate area of rectangle.

def rectangle_area(length, breadth):
    area = length * breadth
    return area

# 2. Write a program to calculate area of circle.

def circle_area(radius):
    area = 3.14 * radius**2
    return area

# 3. Write a program to find sum of following series using functions:
#   a. 1 + 2 + 3 + 4 +..... + n
#   b. 1! + 2! + 3! + 4! +..... + n!
#   c. 1^1 + 2^2 + 3^3 + ...... + n^n

def various_sum(n):
    a = 0
    b = 0
    c = 0
    for i in range(1,n+1):
        a += i
        c += i**i
        fact = i
        for j in range(1,i):
            fact *= j
        b += fact
    
    return n, a, b, c

# 4. Sum of all odd numbers between 1 to n
 
def odd_sum(n):
    sum_of_odds = 0
    for i in range(1,n+1):
        if i%2 != 0:
            sum_of_odds += i
    
    return n, sum_of_odds

# 5. Sum of all prime numbers between 1 to n.

def prime_sum(n):
    x = 1
    sum_of_primes = 0
    for num in range(1,n+1):
        count_divisible = 0
        for j in range(1, x+1):
            if x % j == 0:
                count_divisible += 1
        
        if count_divisible == 2:
            sum_of_primes += x
        else:
            num -= 1
        x += 1
    
    return n, sum_of_primes

# 6. Write a program to find print the following Fibonacci series using functions: 1 1 2 3 5 8...n terms.
# Cannot happen in Type 2

# 7. Write a program to find sum of digits of a number.

def digits_sum(n):
    sum_of_digits = 0
    quo = n
    while(quo != 0):
        rem = quo % 10
        quo = quo // 10
        sum_of_digits += rem 
        
    return n, sum_of_digits

# 8. Write a program find reverse of a number.

def num_reverse(n):
    quo = n
    rev = 0
    while(quo != 0):
        rem = quo % 10
        rev = rev * 10 + rem
        quo = quo // 10
    
    return n, rev
        
# 9. Write a program to check if entered number is a palindrome or not.

def palindrome_or_not(n):
    quo = n
    rev = 0
    while quo > 0:
        rem = quo % 10
        rev = (rev * 10) + rem 
        quo = quo // 10
    
    res = bool(n == rev)
    return n, res

# 10. Write a program to check if entered year is a leap year or not.

def leap_or_not(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                flag = True
            else:
                flag = False
        else:
            flag = True
    else:
        flag = False

    return year, flag

# 11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def armstrong_or_not(num):
    quo = num
    len_of_digits = len(str(num))
    sum_of_power = 0
    while(quo!=0):
        rem = quo % 10
        quo = quo // 10
        sum_of_power += rem ** len_of_digits

    res = sum_of_power == num
    return num, res


rect_area = rectangle_area(4, 3)
print("1. Area of the rectangle =",rect_area)

cir_area = circle_area(7)
print("2. Area of the circle =",cir_area)

n, a, b, c = various_sum(5)
print("3.1. Sum of digits upto",n,"=",a)
print("3.2. Sum of all factorials upto",n,"=",b)
print("3.3. Sum of power series upto",n,"=",c)

n, osum = odd_sum(5)
print("4. Sum of all odd numbers upto",n,"=",osum)

n, psum = prime_sum(10)
print("5. Sum of all primes upto",n,"=",psum)

print("6. Fibonacci series cannot work in Type 4!")

n, dsum = digits_sum(103429)
print("7. Sum of digits of",n,"=",dsum)

n, rev = num_reverse(8765)
print("8. Reverse of",n,"=",rev)

n, pres = palindrome_or_not(n = 12321)
if pres:
    print("9.",n,"is a Palindrome number.")
else:
    print("9.",n,"is not a Palindrome number.")

year, lres = leap_or_not(1900)
if lres:
        print("10.",year,"is a leap year.")
else:
    print("10.",year,"is not a leap year.")

num, ares = armstrong_or_not(153)
if ares:
    print("11.",num,"is an Armtsrong number.")
else:
    print("11.",num,"is not an Armstrong number.")
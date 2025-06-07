


# WAP to solve the following series:
# a. 1!+ 2!+ 3!+ 4!+ .....n!
# b. N+N^2+N^3+N^4.....+N^N (here, ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.(1,2,4,8,16,...)
# d. S = a + a2/2 + a3/3 +......+ a10/10
# e. x - x2/3 + x3/5 - x4/7 +....to n terms

n = int(input("Enter a number: "))
fact = 1 
sum_of_facts = 0
sum_of_expo = 0
sum_of_geo = 0
sum_a = 0
sum_even = 0
sum_odd = 0
i = 1
num = 1
while i != n + 1:
    fact = fact * i
    sum_of_facts = sum_of_facts + fact
    sum_of_expo = sum_of_expo + (n ** i)
    sum_of_geo = sum_of_geo + (i + i)

    sum_a += ((n * i) / i)

    if i % 2 == 0:
        sum_even += ((n * i) / num)
        num += 2
    else:
        sum_odd += ((n * i) / num)
        num += 2        

    i += 1   

print("a. sum of factorials: ",sum_of_facts)
print("b. sum of exponents: ",sum_of_expo)
print("c. sum of geometric series: ",sum_of_geo)
print("d. sum of a thingy: ",sum_a)
print("e. ans =", sum_odd - sum_even)

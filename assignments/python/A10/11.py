# WAP to print all numbers which are divisible by m and n in the list

m = int(input("Enter number 1 to find divisibles: "))
n = int(input("Enter number 2 to find divisibles: "))

l1 = [2,3,4,56,73,27,56,48,99,77,35,64]

for ele in l1:
    if (ele % m == 0) and (ele % n == 0):
        print(ele)
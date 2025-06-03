# Write a program to swap two numbers without using third variable.

n1 = int(input("Enter a number_1: "))
n2 = int(input("Enter a number_2: "))

n1, n2 = n2, n1
print("Swap without third variable =",n1, n2)
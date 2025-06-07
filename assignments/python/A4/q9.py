# WAP to print all numbers in a range divisible by a given number.

start_range = int(input("Enter a number for start of range: "))
end_range = int(input("Enter a number for end of range: "))
n = int(input("Enter the number: "))

for i in range(start_range, end_range + 1):
    if i % n == 0:
        print(i, ": is divisible by ",n)
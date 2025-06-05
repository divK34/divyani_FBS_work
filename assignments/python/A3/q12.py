# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a three digit number: "))

last = num % 10
quo = num // 10
first = quo // 10

if first == last:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")

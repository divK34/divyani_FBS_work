# Write a program to reverse a given number using recursive function.

def reverse_of_num(num, rev):
    if num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        return reverse_of_num(num // 10, rev)
    else:
        return rev

num = int(input("Enter a number: "))
rev = 0
res = reverse_of_num(num, rev)
print("Reverse of",num,"=",res)

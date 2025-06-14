# Python Program to count number of digits and letters in a string.

string1 = "1 2 cha cha 3 2 cha cha"

d_cnt = 0
l_cnt = 0
for s in string1:
    if s.isdigit():
        d_cnt += 1
    elif s.isalpha():
        l_cnt += 1

print("Total number of digits = ",d_cnt)
print("Total number of Letters = ",l_cnt)

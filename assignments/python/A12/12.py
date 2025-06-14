# Python Program to count number of lowercase characters in a string.

string1 = "Python Program to count number of lowercase characters in a string."

lc_count = 0

for s in string1:
    if s.islower():
        lc_count += 1

print("Total Lowercase alphabets in string = ",lc_count)
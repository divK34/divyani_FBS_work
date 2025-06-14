# Python Program to Count the Number of Vowels in a String

string1 = "firstbit solutions, python fullstack with datascience course"
print("og string: ",string1)

count = 0
vowels = "aeiou"

for v in vowels:
    count += string1.count(v)

print("Total number of vowels = ",count)
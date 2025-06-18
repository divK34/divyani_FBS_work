#  Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

s = input("Enter your string = ")
print(s)

words = s.split()

unique_words = set(words)

for word in unique_words:
    cnt = words.count(word)
    print(word,"=",cnt)

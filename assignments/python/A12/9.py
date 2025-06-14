# Python Program to Calculate the Number of Words and the Number of Characters Present in a String 

string1 = "firstbit solutions , python fullstack with datascience course"
print("og string: ",string1)

word_cnt = 0
chr_cnt = len(string1)

for word in string1:
    if word.isalpha():
        word_cnt += 1

print("Word count = ",word_cnt)
print("Character count = ",chr_cnt)
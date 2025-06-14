# Python Program to count the occurrences of ach word in a string

string1 = "actually he has toothache and not stomachache"
print("og string: ",string1)

word = "ach"
str_l = string1.split(" ")

cnt = 0
for w in str_l:
    if word in w:
        cnt += 1
    else:
        cnt += 0 

print(cnt)
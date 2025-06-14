# Python Program to Remove the Characters of Odd Index Values in a String

string1 = "firstbit solutions , python fullstack with datascience course"
print("og string: ",string1)

for i in range(0,len(string1)+1,2):
    print(string1[i], end="")
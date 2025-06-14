# Python Program to Form a New String where the First Character and the Last Character have been Exchanged

string1 = "firstbit solutions, python fullstack with datascience course"
print("og string: ",string1)

first = string1[0]
print("First character = ",first)

last = string1[-1]
print("Last character = ",last)

fr = last + string1[1:]
lr = fr[:-1] + first
print(lr)
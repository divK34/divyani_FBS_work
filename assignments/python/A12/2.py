# Python Program to Remove the nth Index Character from a Non-Empty String

n = int(input("Enter the index to be removed: "))
string1 = "firstbit solutions, python fullstack with datascience course"
print("og string: ",string1)

ns = string1[:n] + string1[n+1:]
print("removed the charactyer at",n,"th index:",ns)
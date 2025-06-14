# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

def get_len(s):
    str_len = 0
    for i in s:
        str_len += 1
    return str_len

string1 = input("Enter first string = ")
string2 = input("Enter second string = ")

len_string1 = get_len(string1)
len_string2 = get_len(string2)

if len_string1 > len_string2:
    print(string1)
    print("string 1 is larger than string 2")
else:    
    print(string2)
    print("string 2 is larger than string 1")


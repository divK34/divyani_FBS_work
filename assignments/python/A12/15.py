# Python Program to find larger string without using built-in functions.  

def get_len(s):
    str_len = 0
    for i in s:
        str_len += 1
    return str_len

def get_strings(n):
    str_list = []
    for i in range(n):
        string1 = input("Enter the string = ")
        str_list.append(string1)
    
    str_ll = []
    for s in str_list:
        str_len = get_len(s) 
        str_ll.append(str_len)
    
    return str_list, str_ll 

def check_larger(n):
    str_list, str_len_list = get_strings(n)

    largest_index = 0
    max_length = str_len_list[0]

    for i in range(1, n):
        if str_len_list[i] > max_length:
            max_length = str_len_list[i]
            largest_index = i
    
    print("Largest string of all is:")
    print(str_list[largest_index])

n = int(input("Enter total number of strings = "))
check_larger(n)

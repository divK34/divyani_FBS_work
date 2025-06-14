# Python Program to Check if a Given Key Exists in a Dictionary or Not

k = "sachin"
my_dict = {"roll_no":10,
           "name":"sachin",
           "marks":150,
           "gender":"male"}

if k in my_dict.keys():
    print(k,"is a key in dictionary.")
elif k in my_dict.values():
    print(k,"is a value in dictionary.")
else:
    print(k,"doesnt exist in dictionary.")
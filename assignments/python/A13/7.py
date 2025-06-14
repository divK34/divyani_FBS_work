# Python Program to Remove the Given Key from a Dictionary.

d = {"name":"xyv",
     "c_id" :101,
     "gender":"male",
     "age":29}
print("dictionary =",d)

k = input("Enter the key to be removed: ")
if k in d:
    d.pop(k)
    print("new dictionary =",d)
else:
    print(k,"is not in dictionary.")
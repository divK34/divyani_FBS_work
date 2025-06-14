# Python Program to Concatenate Two Dictionaries Into One

dict1 = {"artist":"adele",
         "album":"21",
         "year":2016}

dict2 = {"total songs":9}

print("dict 1 = ",dict1)
print("dict 2 = ",dict2)
dict1.update(dict2)

print("concatenation of dictionaries =")
print(dict1)
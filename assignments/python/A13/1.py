# Python Program to Add a Key-Value Pair to the Dictionary

my_dict = {"name":"james bond",
           "roll_no":101,
           "class":10}
key_list = []
for key in my_dict.keys():
    key_list.append(key)
print("all keys = ",key_list)
print()

value_list = []
for value in my_dict.values():
    value_list.append(value)
print("all values = ",value_list)
print()

for key, value in my_dict.items():
    print(key,"=",value)
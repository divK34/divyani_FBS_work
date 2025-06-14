# Python Program to Multiply All the Items in a Dictionary

d = {1:2,
     2:4,
     3:6,
     4:8}
print("dictionary =",d)

key_mul = 1
value_mul = 1

for key, value in d.items():
    key_mul *= key
    value_mul *= value

print("multiplication of all keys =",key_mul)
print("multiplication of all values =",value_mul)
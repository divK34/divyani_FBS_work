# Python Program to Sum All the Items in a Dictionary.

d = {1:2,
     2:4,
     3:6,
     4:8}
print("dictionary =",d)
key_sum = 0
value_sum = 0

for key, value in d.items():
    key_sum += key
    value_sum += value

print("sum of all keys =",key_sum)
print("sum of all values =",value_sum)
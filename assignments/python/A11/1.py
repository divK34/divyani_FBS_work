# Python Program to Put Even and Odd elements of a List into two Different Lists
l1 = [1,2,3,4,5,6]

el = []
ol = []

for i in l1:
    if i % 2 == 0 :
        el.append(i)
    else:
        ol.append(i)

print("even list =",el)
print("odd list =",ol)
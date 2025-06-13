# Python Program to Sort the List According to the Second Element in Sublist
lol = [["sachin",10,150],["virat",18,180],["dhoni",7,200]]

for i in range(len(lol)):
    mi = i
    for j in range(i+1,len(lol)):
        if lol[j][1] < lol[mi][1]:
            mi = j
    lol[i], lol[mi] = lol[mi], lol[i]
print(lol)

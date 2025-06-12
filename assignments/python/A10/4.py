# WAP to reverse the list
l1 = [10, 20, 30, 40, 50]
rev = []

for k in range(len(l1)-1,-1,-1):
    rev.append(l1[k])

print("Reverse of",l1,"is",rev)
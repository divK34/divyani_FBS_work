# WAP of having n number of elements in the list 
# and find out even and odd elements in that list 
# and then create two separate lists which will have even elements and other will have odd elements.

l1 = []
n = int(input("Enter the no of element: "))

for _ in range(n):
    ele = int(input("Enter the element: "))
    l1.append(ele)

even = []
odd = []
for ele in l1:
    if ele % 2 == 0:
        even.append(ele)
    else:
        odd.append(ele)

print("Even list: ",even)
print("Odd list: ",odd)
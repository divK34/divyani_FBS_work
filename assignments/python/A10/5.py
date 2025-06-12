# Accept a number from user and check if this element is present in the list or not. 
# Also tell how many times it is present in the list.

def n_in_l(n, l1):
    cnt = 0
    for ele in l1:
        if ele == n:
            cnt += 1
    return cnt

n = int(input("Enter a number: "))
l1 = [10, 99, 73, 46, 102, 746, 88, 89, 56, 54, 32, 32]

if n in l1:
    cnt = n_in_l(n, l1)
    print(n,"is present in list, about", cnt,"times.")
else:
    print(n,"is not present in list.")
# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n = int(input("Enter number: "))
res_dict = {}

for i in range(1,n+1):
    res_dict.update({i:i*i})

print(res_dict)
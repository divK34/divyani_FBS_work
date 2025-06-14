# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary. 

d = {"name":"xyv",
     "c_id" :101,
     "gender":"age",
     "age":29}
print("og dictionary =",d)

w = input("Enter word for frequency check = ")

k_lst = []
v_lst = []
k_w_sum = 0
v_w_sum = 0

for k,v in d.items():
    k_lst.append(k)
    v_lst.append(v)

if w in k_lst or w in v_lst:
    k_w_sum += k_lst.count(w)
    v_w_sum += v_lst.count(w)   
else:
    print(w,"does not exist in dictionary.")

w_sum = k_w_sum + v_w_sum 
if w_sum > 0:
    print(w,"occurs",w_sum,"times in dictionary.")
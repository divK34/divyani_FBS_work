# Write a program to calculate the m to the power n using recursion.
# m = 3, n = 2, m*m

def mtn(m, n, res, i):
    if i <= n:
        res *= m
        return mtn(m, n, res, i+1)
    else:
        return res

m = 5
n = 2
res = 1
i = 1
res = mtn(m, n, res, i)
print(res)
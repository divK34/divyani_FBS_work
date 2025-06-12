# 1.Write a program to find sum of following series using recursive functions:
# i. 1! + 2!  + 3! + 4! + ..... + n! 
# Note : For fact and sum two recursive functions

def factorial(i, n, sum, fact):
    if i <= n:        
        fact *= i  
        sum += fact      
        return factorial(i+1, n, sum, fact)    
    else:
        return sum

n = int(input("Enter the number: "))
i = 1
sum = 0
fact = 1

res = factorial(i, n, sum, fact)
print("sum of factorials series till",n,"=",res)
# 1.  We want to generate Fibonacci numbers up to a certain limit. Instead of computing and storing the entire sequence in memory, create generator to yield Fibonacci numbers one by one, conserving memory and allowing for easy iteration. 
# def fibo(n, f0, f1):
#     while n != 0:
#         yield f0
#         f0, f1 = f1, f0 + f1
#         n -= 1

# n = 10
# f0 = 0
# f1 = 1
# res = fibo(n, f0, f1)
# for i in res:
#     print(i, end=" ")

# 2.  Implement a generator function that yields palindrome numbers. Palindromes are numbers that read the same backward as forward (e.g., 121, 1331). Generate palindromes lazily and infinitely. 

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# def palindrome_generator():
#     n = 0
#     while True:
#         if is_palindrome(n):
#             yield n
#         n += 1

# # prints first 20 palindromes
# gen = palindrome_generator()
# for _ in range(20):
#     print(next(gen), end=" ")

# 3.  Write a generator function that mimics the behavior of the built-in range() function. The generator should take start, stop, and step arguments and yield numbers within the specified range. 

def ranger(start, stop, step=1):
    if step == 0:
        print("step must not be zero")
    
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

res = ranger(5, 0, -1)
for i in res:
    print(i, end=" ")

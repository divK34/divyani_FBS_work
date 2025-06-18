# Develop a memoization decorator that caches the results of function calls and returns the cached result when the same inputs occur again. This can greatly improve the performance of recursive or computationally intensive functions.

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args[0]}")
            return cache[args]
        print(f"Calculating {args[0]}")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("Fibonacci values:")
for i in range(15):
    print(f"{i}: {fib(i)}")


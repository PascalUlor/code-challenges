"""
---Fibonacci---
f(n) = f(n-1) + f(n-2)
for n => Natural numbers
start values:
    f(0) = 0
    f(1) = 1
"""
def fibonacci(n, fib_arr=[0,1]):
    if n <= 0:
        return fib_arr[0:]

    if n <= len(fib_arr):
        return fib_arr[n-1]
    nth_fib = fibonacci(n-1) + fibonacci(n-2)
    fib_arr.append(nth_fib)
    print(fib_arr)
    return nth_fib


fibonacci(8)
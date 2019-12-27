def memoize(func):
    cache = dict()
    print('1111111', cache)

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


import timeit
# log = timeit.timeit('fibonacci(35)', globals=globals(), number=1)

memoized_fibonacci = memoize(fibonacci)
log = timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1)

print(log)

cache = memoized_fibonacci.__closure__[0].cell_contents
# print('cache', cache)
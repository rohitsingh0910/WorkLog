def memoize(f):
    cache = {}
    def g(*args, **kwargs):
        k = (args, tuple(sorted(kwargs.items())))
        if k not in cache:
            cache[k] = f(*args, **kwargs)
        return cache[k]
    return g

@memoize
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print(fib(35))

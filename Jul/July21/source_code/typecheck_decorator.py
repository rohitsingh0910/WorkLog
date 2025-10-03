from functools import wraps
import inspect

def typecheck(f):
    sig = inspect.signature(f)
    hints = f.__annotations__
    @wraps(f)
    def g(*a, **k):
        bound = sig.bind(*a, **k)
        for name, val in bound.arguments.items():
            if name in hints and not isinstance(val, hints[name]):
                raise TypeError(name)
        r = f(*a, **k)
        if 'return' in hints and not isinstance(r, hints['return']):
            raise TypeError('return')
        return r
    return g

@typecheck
def concat(a: str, b: str) -> str:
    return a + b

if __name__ == "__main__":
    print(concat("hi", "there"))

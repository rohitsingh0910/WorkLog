import time
import random

def retry(times, base):
    def outer(f):
        def inner(*a, **k):
            t = times
            d = base
            while t:
                try:
                    return f(*a, **k)
                except Exception:
                    time.sleep(d)
                    d *= 2
                    t -= 1
            raise
        return inner
    return outer

@retry(3, 0.1)
def flaky():
    if random.random() < 0.7:
        raise ValueError
    return "ok"

if __name__ == "__main__":
    print(flaky())

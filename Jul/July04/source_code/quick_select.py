import random

def quickselect(a, k):
    if len(a) == 1:
        return a[0]
    pivot = random.choice(a)
    lows = [x for x in a if x < pivot]
    highs = [x for x in a if x > pivot]
    pivots = [x for x in a if x == pivot]
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

if __name__ == "__main__":
    arr = [9,1,5,3,7,2,8,6,4]
    print(quickselect(arr, 4))

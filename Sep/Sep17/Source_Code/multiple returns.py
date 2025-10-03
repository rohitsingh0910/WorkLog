def func(x, y, z=0):
    if z > 10:
        return x + y
    return x - y
print(func(5, 3))   # Call 1
print(func(5, 3, 11))   # Call 2
print(func(5, 3, -1))   # Call 3
print(func(5, 3, 10))   # Call 4

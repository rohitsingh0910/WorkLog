def process_items(*items, **info):
    total = sum(items)
    return total, info.get("name", "Unknown")

print(process_items(1, 2, 3, name="Rohit", age=22))

#---------------------------------------------------------

def func(x, *args, y=2, z=3, **kwargs):
    print(f"x: {x}, args: {args}, y: {y}, z: {z}, kwargs: {kwargs}")

func(1, 2, 3, 4, y=10, a=5, b=6)

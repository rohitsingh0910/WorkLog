def func_args_example(a, b=2, *args, **kwargs):
    return a + b + sum(args) + sum(kwargs.values())

x = 10
def shadow_example():
    x = 5
    return x

def scope_example():
    global x
    x = x + 1
    return x

def mutable_default(arg=[]):
    arg.append(1)
    return arg

def immutable_default(val=0):
    val += 1
    return val

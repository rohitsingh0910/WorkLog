Function Arguments Overview:
a) Default Arguments:

Default arguments are used when you don't pass a value to the function parameter. If not provided, the default value is used.

Edge case: When mutable objects like lists or dictionaries are used as default arguments, it can lead to unintended behavior, because they retain changes across function calls.

Example:

def add_item(item, items_list=[]):  
    items_list.append(item)
    return items_list

print(add_item("apple"))  # ['apple']
print(add_item("banana")) # ['apple', 'banana'] (Not expected behavior)


Key Insight:
Default arguments are evaluated once when the function is defined, not each time the function is called.

b) Positional & Keyword Arguments:

Positional arguments are required and passed in the order of parameters.

Keyword arguments allow you to specify the name of the argument when calling the function, so the order doesn’t matter.

Edge case: Mixing positional and keyword arguments incorrectly will throw a SyntaxError.

Example:

def func(a, b, c):
    print(a, b, c)

# Correct
func(1, b=2, c=3)  # 1 2 3


Mixing positional and keyword arguments incorrectly:

func(1, c=3, 2)  # SyntaxError: positional argument follows keyword argument

c) Variable-Length Arguments:

*args: Used to pass a variable number of positional arguments as a tuple.

**kwargs: Used to pass a variable number of keyword arguments as a dictionary.

Edge cases for *args and **kwargs:

If no arguments are passed, args will be an empty tuple and kwargs will be an empty dictionary.

args can only hold positional arguments, and kwargs holds keyword arguments.

*args must be before **kwargs in the function signature.

Example for *args and **kwargs:

def demo(x, *args, **kwargs):
    print("x:", x)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, a=10, b=20)
# Output:
# x: 1
# args: (2, 3)
# kwargs: {'a': 10, 'b': 20}



-----------------------------------------------------------------------------------


What is the signature module?

The inspect.signature() function from the inspect module allows you to retrieve the signature of a function. The signature provides details like:

The function’s name

The number and names of its parameters

Default values (if any)

Whether a parameter is positional, keyword-only, or variadic

Why use the signature module?

Imagine you're building a dynamic system, like a web framework or a plugin system, where you need to:

Validate and manage function arguments programmatically.

Generate documentation or automatically configure function calls.

Handle user input dynamically based on the function signature.

The signature module lets you inspect any function's signature so that you can handle arguments appropriately, especially in flexible or abstracted environments.

Basic Example
import inspect

def greet(name, message="Hello"):
    return f"{message}, {name}!"

# Get the signature of the function
sig = inspect.signature(greet)

print(sig)  # Output: (name, message='Hello')


Here, we used inspect.signature() to retrieve the function's signature, which shows:

The required parameter name

The optional parameter message with its default value Hello

Exploring the Signature in Detail

Now that we have the signature, we can break it down to access each parameter.

# Inspect each parameter individually
for param in sig.parameters.values():
    print(param.name, param.kind, param.default)


Output:

name POSITIONAL_OR_KEYWORD <class 'inspect._empty'>
message POSITIONAL_OR_KEYWORD Hello


name is a positional or keyword parameter, meaning you can pass it either positionally or by keyword.

message is also a positional or keyword parameter, but it has a default value of "Hello".

Types of Parameter Kinds in signature

The param.kind attribute can return different types of parameter kinds:

POSITIONAL_ONLY: The parameter can only be passed as a positional argument.

KEYWORD_ONLY: The parameter can only be passed as a keyword argument.

VAR_POSITIONAL (*args): The parameter can accept any number of positional arguments.

VAR_KEYWORD (**kwargs): The parameter can accept any number of keyword arguments.

POSITIONAL_OR_KEYWORD: The parameter can be passed either as a positional or keyword argument.

Example with Various Kinds
def complex_func(a, b=10, *args, kw1, kw2='default', **kwargs):
    pass

sig = inspect.signature(complex_func)
for param in sig.parameters.values():
    print(f"{param.name}: {param.kind}, Default: {param.default}")


Output:

a: POSITIONAL_OR_KEYWORD, Default: <class 'inspect._empty'>
b: POSITIONAL_OR_KEYWORD, Default: 10
args: VAR_POSITIONAL, Default: <class 'inspect._empty'>
kw1: KEYWORD_ONLY, Default: <class 'inspect._empty'>
kw2: KEYWORD_ONLY, Default: default
kwargs: VAR_KEYWORD, Default: <class 'inspect._empty'>

Practical Use Cases of the signature Module

Dynamic Function Invocation

Imagine you’re creating a function that dynamically calls another function based on the signature. You could validate the arguments before calling the function.

def dynamic_call(func, *args, **kwargs):
    sig = inspect.signature(func)
    bound_args = sig.bind(*args, **kwargs)  # Binds arguments to the function's signature
    bound_args.apply_defaults()  # Applies default values where necessary

    print("Arguments to pass:", bound_args.arguments)
    return func(*bound_args.args, **bound_args.kwargs)

def add(a, b=5):
    return a + b

result = dynamic_call(add, 3)
print(result)  # Output: 8 (because b gets the default value of 5)


Validating Arguments

You could check whether the correct type of arguments is passed to a function, ensuring that it's safe to call it.

def validate_args(func, *args, **kwargs):
    sig = inspect.signature(func)
    for param, value in zip(sig.parameters.values(), args):
        if param.annotation != inspect.Parameter.empty:
            if not isinstance(value, param.annotation):
                raise TypeError(f"Argument {param.name} must be of type {param.annotation}")
    return func(*args, **kwargs)

def greet(name: str, age: int):
    return f"Hello, {name}. You are {age} years old."

print(validate_args(greet, "Alice", 30))  # This will work
# validate_args(greet, "Alice", "thirty")  # This will raise a TypeError


Generating Documentation

If you need to generate function documentation automatically, you can use the signature to extract parameter names and default values.

def generate_doc(func):
    sig = inspect.signature(func)
    doc = f"Function '{func.__name__}' accepts the following parameters:\n"
    for param in sig.parameters.values():
        doc += f"- {param.name}: {param.default if param.default != inspect.Parameter.empty else 'No default'}\n"
    return doc

def sample_func(x, y=10, z="default"):
    pass

print(generate_doc(sample_func))


Output:

Function 'sample_func' accepts the following parameters:
- x: No default
- y: 10
- z: default

Edge Cases to Consider

Empty Default Parameter:
When a parameter does not have a default value, param.default will be set to inspect.Parameter.empty.

def my_func(a, b=2):
    pass

sig = inspect.signature(my_func)
print(sig.parameters['a'].default)  # Output: <class 'inspect._empty'>


Bound Arguments:
When using bind() to bind arguments, make sure the correct number of arguments is passed, or it will raise a TypeError.

Compatibility:
Some functions, especially those wrapped in decorators, may not directly support introspection using inspect.signature(). In these cases, you might need to handle exceptions or unwrap the decorator.
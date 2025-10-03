A decorator is a function that takes another function (or method) as an argument, modifies or extends its behavior, and then returns a new function. It allows you to add functionality to an existing function or method without modifying its code directly.

Think of a decorator as a gift wrapper. When you have a present (your function), a decorator wraps it with an additional layer (extra functionality) without changing the present itself.

Basic Syntax of a Decorator

A decorator is typically written as a function that takes another function and returns a new function. Here’s the basic syntax:

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before the original function")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()


Here’s how this works:

display() is the original function.

decorator_function takes the original function as an argument and returns a wrapper_function, which modifies or extends the behavior of the original function.

The @decorator_function syntax is shorthand for passing display() into decorator_function and reassigning display() to the returned wrapper_function.

Real-World Analogy

Let’s think of a restaurant example:

Imagine you run a restaurant and you have a chef who prepares dishes (functions).

Now, you want to add a feature where every dish is checked for allergies before serving. Instead of modifying the recipe for each dish, you create a decorator (let’s call it the "allergy check").

The decorator will wrap the dish, check for allergies, and then serve it.

So, the decorator in this analogy is like an allergy check that’s added to all dishes but doesn’t alter the original recipe.

Step-by-Step Example

Let’s break down a simple decorator that prints a message before and after a function executes:

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

def say_hello():
    print("Hello!")

# Applying the decorator
decorated_function = my_decorator(say_hello)
decorated_function()


Output:

Before function execution
Hello!
After function execution


Here’s what happens:

my_decorator(say_hello) is called, returning the wrapper function.

The wrapper function adds extra behavior (printing the messages) before and after calling the original function say_hello.

You can also use the @ syntax to simplify this:

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


This is equivalent to:

say_hello = my_decorator(say_hello)

Multiple Decorators

You can stack multiple decorators to modify the behavior of a function in several layers:

def decorator1(func):
    def wrapper():
        print("Decorator 1 - Before")
        func()
        print("Decorator 1 - After")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 - Before")
        func()
        print("Decorator 2 - After")
    return wrapper

@decorator1
@decorator2
def greet():
    print("Hello!")

greet()


Output:

Decorator 1 - Before
Decorator 2 - Before
Hello!
Decorator 2 - After
Decorator 1 - After


greet is first wrapped by decorator2, and then that wrapped function is passed to decorator1.

Decorators with Arguments

Decorators can also take arguments. If you want to pass arguments to the decorator, you need to make the decorator return another function that accepts arguments.

Example: Decorator with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")


Output:

Hello, Alice!
Hello, Alice!
Hello, Alice!


repeat(3) is the decorator that takes an argument n, and the wrapper function calls the say_hello function n times.

Decorators with Return Values

Decorators can also modify the return value of the original function:

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # Output: HELLO, ALICE


uppercase_decorator changes the return value of greet() to uppercase.

Real-World Use Case of Decorators

Let’s build a logging decorator to track function calls, just like how logging middleware works in web frameworks.

Example: Logging Decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(a, b):
    return a * b

# Calling the functions
print(add(3, 4))  # Output: Function add called with arguments: (3, 4) {}
print(multiply(2, 5))  # Output: Function multiply called with arguments: (2, 5) {}


Output:

Function add called with arguments: (3, 4) {}
7
Function multiply called with arguments: (2, 5) {}
10


Here, we added logging functionality to both the add and multiply functions, without modifying the original functions themselves.

Edge Cases and Best Practices

Using functools.wraps:
When you apply decorators, it’s a good practice to use functools.wraps to preserve the original function's metadata (like name, docstring, etc.).

from functools import wraps

def decorator_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


This ensures that the decorated function has the same name and docstring as the original function.

Order of Decorators:
The order of decorators matters. The decorator closest to the function (the one on top) gets applied first. This can affect the final result.

Decorators with State:
If your decorator needs to maintain state (e.g., counting how many times a function is called), you can do this by defining state inside the decorator.

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function {func.__name__} called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def greet():
    print("Hello!")

greet()  # Output: Function greet called 1 times
greet()  # Output: Function greet called 2 times

Summary

Decorators are functions that modify or extend the behavior of another function.

They are defined as a function that takes a function and returns a new function (the "wrapper").

@decorator_name is shorthand for applying a decorator to a function.

You can stack multiple decorators, pass arguments to decorators, and modify return values.

Common use cases include logging, timing, and validation.

Always use functools.wraps to preserve function metadata when using decorators.
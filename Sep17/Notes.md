Namespace

a namespace is a container that holds names (identifiers like variable names, function names, class names, etc.) and maps them to the corresponding objects (like values or functions). It's how Python keeps track of all the variables and their values in a program.

Think of a namespace like a dictionary:
{
    'x': 10,
    'print': <built-in function print>,
    'my_function': <function my_function at 0x...>
}

Types of Namespaces in Python

Python has different types of namespaces depending on the scope:

1.Built-in Namespace

Contains built-in functions and exceptions like len(), print(), Exception, etc.

Available everywhere in your code.

2.Global Namespace

Created when a module is loaded.

Contains functions, variables, and classes defined at the top level of a script or module.

3.Local Namespace

Created when a function is called.

Contains the variables defined inside the function.

4.Enclosing Namespace (Closure)

Exists in nested functions.

Contains the namespace of the outer function.

Edge Cases of Default, Positional & Keyword Arguments
✅ Basic Rule Recap:

Positional arguments must come before keyword arguments.

Default arguments must follow non-default arguments.
#--------------set discard---------------------

new_set={1,2,3,4,5}
new_set.discard(3)
print(new_set)

#-----------nested comprehension + scope---------------------

x = 5
lst = [x for x in range(3)]
print(x)

#------------mutability & aliasing -------------------

def func(a, L=[]):
    L.append(a)
    return L

print(func(1))
print(func(2))
print(func(3))

#--------------------List Comprehension with Condition + Matrix Logic--------------------

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [row[i] for row in matrix for i in range(len(row)) if row[i] % 2 == 0]
print(result)

#---------------- 2D Conditional Mapping -------------------

result = [[i * j for j in range(1, 4) if i != j] for i in range(1, 4)]
print(result)

#--------------- Scope of variable ----------------------
x=30
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print(x)

x=30
def outer():
    x = 10
    def inner():
        global x
        x = 20
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("very outer",x)
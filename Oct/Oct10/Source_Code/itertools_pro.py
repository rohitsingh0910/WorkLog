from itertools import product, repeat

a = list(map(int, input().strip().split()))
# print(a)
b = list(map ( int , input().strip().split()))
# print(b)
for items in product(a,b):
    print(items,end=" ")

c=[1,2,3]

print(list(product(a,repeat=2)))
for items in product(a,b,c):
    print(items,end=" ")
from collections import Counter
X=int(input())
a=list(map(int,input().strip().split()))
# print(a)
c=Counter(a)
# print(c.items())
per=int(input())
earn=0
for _ in range(per):
    size,price=map(int,input().strip().split())
    if c[size]>0:
        c[size]-=1
        earn+=price
print(earn)
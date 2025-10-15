t=int(input())
dic={}
count=0
for _ in range(t):
    new=input()
    if new in dic:
        dic[new]+=1
    else:
        dic[new]=1
        count+=1
print(count)
for i in dic.values():
    print(i,end=" ")
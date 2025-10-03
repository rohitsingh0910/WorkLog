lis=[[1,2,3],[4,5,6],[7,8,9]]

# out=[[1,2,4],[2,3,5],[3,4,6]]

out=[]
s=[]
for i in range(len(lis)):
    for j in range(len(lis)):
        s.append(lis[j][i])
    out.append(s)
print(out)
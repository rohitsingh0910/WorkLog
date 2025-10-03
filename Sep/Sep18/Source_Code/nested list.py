if __name__ == '__main__':
    lis=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([score,name])
    lis.sort(key=lambda x:x[0])
    dic={}
    for i,j in lis:
        if i in dic.keys():
            dic[i]=dic[i].append(j)
        else:
            dic[i]=j
    print(dic)

lis=[]
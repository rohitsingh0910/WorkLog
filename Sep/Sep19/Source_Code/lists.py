if __name__ == '__main__':
    N = int(input())
    output=[]
    for _ in range(N):
        lis=input().strip().split()
        if lis[0]=="insert":
            output.insert(int(lis[1]),int(lis[2]))
        elif lis[0]=="print":
            print(output)
        elif lis[0]=="remove":
            output.remove(int(lis[1]))
        elif lis[0]=="append":
            output.append(int(lis[1]))
        elif lis[0]=="sort":
            output.sort()
        elif lis[0]=="pop":
            output.pop()
        elif lis[0]=="reverse":
            output.reverse()
        else:
            continue


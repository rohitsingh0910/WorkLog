word,num=input().strip().split()
num=int(num)
# print(word, num)
from itertools import permutations
# lis=word.split()
lis=list(permutations(word,num))
out_lis=sorted(lis)
for i in out_lis:
    print("".join(i))
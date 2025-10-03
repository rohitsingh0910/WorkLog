# lis=[1,2,3,4,5,6]
# lenlis=len(lis)
# result = []
# for i in range(lenlis):
#     for j in range(i,lenlis):
#         result.append(lis[i:j+1])
# print(result)

lis = [1, 2, 3, 4, 5, 6]
# n = len(lis)
# result = []
# for i in range(1, 2**n):
#     subset = []
#     for j in range(n):
#         if (i >> j) & 1:
#             subset.append(lis[j])
#     result.append(subset)
# for i in result:
#     if sum(i)==10:
#         print(i)

l1=[1,2,3,4,5,6]
subarray=[[]]
s=[]
print(subarray)
for i in l1:
    new=[]
    for j in subarray:
        new.append(j+[i])
        # if sum(j + [i]) == 10:
        #     s.append(list(j+[i]))

    subarray.extend(new)
print(subarray)
# print(s)
# def subarrayBitwiseORs( arr):
#     r = []  # stores the OR results
#     l = 1  # index of the last result at the start
#     for i in arr:
#         ri = len(r)  # length of the results so far
#         r.append(i)  # start a new OR result with the current element
#         for j in range(l, ri):
#             v = r[j] | i  # OR the current value with previous results
#             if r[-1] != v:  # Avoid adding duplicate OR results
#                 r.append(v)
#         l = ri  # update the last index after this iteration
#     return len(set(r))  # return the count of unique OR results
# print(subarrayBitwiseORs([1,2,4]))
arr=[1,2,4]
lenlis = len(arr)
result = []
for i in range(lenlis):
    for j in range(i, lenlis):
        result.append(arr[i:j + 1])
print(result)
lis=[]
for i in result:
    s=0
    for j in i:
        s|=j
    lis.append(s)
print(len(set(lis)))
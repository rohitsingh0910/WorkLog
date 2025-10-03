nums = [1,2]
maximum=max(nums)
# print(maximum)

final=[]

for i in range(len(nums)):
    s = []
    add = 0
    for j in range(i,len(nums)):
        add+=nums[j]
        s.append(j)
        if add>=maximum:
            break
    final.append(len(s))
print(final)
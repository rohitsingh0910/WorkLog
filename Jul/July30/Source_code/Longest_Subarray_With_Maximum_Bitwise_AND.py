def longestSubarray(nums):
    num = max(nums)
    maxlen = 0
    currentlen = 0
    for i in nums:
        if i == num:
            currentlen += 1
            maxlen = max(maxlen, currentlen)
        else:
            currentlen = 0
    return maxlen


nums = [1,2,3,3,2,2]
print(longestSubarray(nums))
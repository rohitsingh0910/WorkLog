def smallestSubarrays(nums):
        n = len(nums)
        answer = [1] * n
        last = [-1] * 30

        for i in range(n-1, -1, -1):
            x = nums[i]
            for bit in range(30):
                if x >> bit & 1:
                    last[bit] = i

            max_j = i
            for bit in range(30):
                if last[bit] != -1:
                    max_j = max(max_j, last[bit])

            answer[i] = max_j - i + 1

        return answer
nums=[1,2,3,4,5,1,2]
print(smallestSubarrays(nums))
def time_conversion(s):
    hour = int(s[:2])
    if s[-2:] == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    return f"{hour:02d}{s[2:8]}"

def find_runner_up(scores):
    scores = list(set(scores))
    scores.sort(reverse=True)
    return scores[1]

def remove_duplicates(nums):
    if not nums:
        return 0
    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1
    return index

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

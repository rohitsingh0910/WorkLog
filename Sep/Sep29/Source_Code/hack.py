def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

def swap_case(s):
    return ''.join([c.lower() if c.isupper() else c.upper() for c in s])

def second_highest(nums):
    nums = list(set(nums))
    nums.sort(reverse=True)
    return nums[1] if len(nums) > 1 else None

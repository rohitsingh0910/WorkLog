def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

def is_valid_parentheses(s):
    stack = []
    mapping = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            if not stack or mapping[stack.pop()] != char:
                return False
    return not stack

def merge_sorted_arrays(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]




def is_anagram(s, t):
    return sorted(s) == sorted(t)

def reverse_words(s):
    return ' '.join(s.strip().split()[::-1])

def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits




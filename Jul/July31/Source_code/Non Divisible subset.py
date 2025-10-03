def nonDivisibleSubset(k, s):
    remainder_count = [0] * k
    for num in s:
        remainder_count[num % k] += 1

    result = min(remainder_count[0], 1)
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            result += max(remainder_count[i], remainder_count[k - i])
        else:
            result += min(remainder_count[i], 1)

    return result
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))

result = nonDivisibleSubset(k, s)
print(result)
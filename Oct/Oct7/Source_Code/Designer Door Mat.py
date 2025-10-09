n, m = map(int, input().strip().split())
welcome_str = "WELCOME"
mid = n // 2 + 1

for i in range(1, n + 1):
    if i == mid:
        print(welcome_str.center(m, '-'))
    else:
        if i < mid:
            pattern_count = 2 * i - 1
        else:
            pattern_count = 2 * (n - i) + 1
        pattern = ".|." * pattern_count
        print(pattern.center(m, '-'))

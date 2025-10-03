def binary_insort(a, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if a[mid] < val:
            start = mid + 1
        else:
            end = mid
    a.insert(start, val)

def merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:]); out.extend(b[j:])
    return out

def sort_like_timsort(a):
    i = 0
    runs = []
    n = len(a)
    while i < n:
        run = [a[i]]
        i += 1
        while i < n and a[i] >= run[-1]:
            run.append(a[i]); i += 1
        for k in range(1, len(run)):
            binary_insort(run, run.pop(k), 0, k)
        runs.append(run)
    while len(runs) > 1:
        b = runs.pop()
        a = runs.pop()
        runs.append(merge(a, b))
    return runs[0]

if __name__ == "__main__":
    print(sort_like_timsort([5,3,1,2,9,8,7,6,4]))

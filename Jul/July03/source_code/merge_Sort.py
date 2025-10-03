def merge_sort(a, key=lambda x: x):
    if len(a) < 2:
        return a
    m = len(a) // 2
    left = merge_sort(a[:m], key)
    right = merge_sort(a[m:], key)
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

if __name__ == "__main__":
    data = ["Banana", "apple", "cherry", "Apricot", "banana"]
    print(merge_sort(data, key=lambda s: (s.lower(), len(s))))

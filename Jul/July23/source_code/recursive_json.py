def diff(a, b, path=()):
    if type(a) != type(b):
        return [(path, a, b)]
    if isinstance(a, dict):
        out = []
        keys = set(a) | set(b)
        for k in keys:
            if k not in a or k not in b:
                out.append((path + (k,), a.get(k), b.get(k)))
            else:
                out.extend(diff(a[k], b[k], path + (k,)))
        return out
    if isinstance(a, list):
        out = []
        n = max(len(a), len(b))
        for i in range(n):
            va = a[i] if i < len(a) else None
            vb = b[i] if i < len(b) else None
            if va is None or vb is None:
                out.append((path + (i,), va, vb))
            else:
                out.extend(diff(va, vb, path + (i,)))
        return out
    return [] if a == b else [(path, a, b)]

if __name__ == "__main__":
    x = {"a":[1,2,{"z":3}],"b":5}
    y = {"a":[1,4,{"z":3}],"b":6,"c":7}
    for d in diff(x,y):
        print(d)

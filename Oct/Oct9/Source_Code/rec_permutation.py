from collections import Counter

def multiset_permutations(seq):
    c = Counter(seq)
    res = []
    def dfs(path, left):
        if left == 0:
            res.append(tuple(path))
            return
        for k in list(c.keys()):
            if c[k]:
                c[k] -= 1
                path.append(k)
                dfs(path, left - 1)
                path.pop()
                c[k] += 1
    dfs([], len(seq))
    return res

if __name__ == "__main__":
    print(len(multiset_permutations("aabc")))

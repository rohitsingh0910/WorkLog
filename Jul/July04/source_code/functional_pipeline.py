from functools import reduce

data = ["This", "is", "a", "sample", "text", "with", "Mixed", "CASE", "letters"]
res = reduce(lambda acc, x: acc + [x.lower()], filter(lambda w: len(w) > 2, data), [])
freq = reduce(lambda d, w: (d.update({w: d.get(w, 0) + 1}) or d), res, {})
print(sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])))

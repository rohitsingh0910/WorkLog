from collections import deque, defaultdict

def topo(edges):
    g = defaultdict(list)
    indeg = defaultdict(int)
    nodes = set()
    for u,v in edges:
        g[u].append(v)
        indeg[v] += 1
        nodes.add(u); nodes.add(v)
    q = deque([n for n in nodes if indeg[n] == 0])
    out = []
    while q:
        u = q.popleft()
        out.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(out) != len(nodes):
        raise ValueError
    return out

print(topo([('a','b'),('b','c'),('a','c')]))

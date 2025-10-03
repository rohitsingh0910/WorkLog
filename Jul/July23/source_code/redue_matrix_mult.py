from functools import reduce

def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x*y for x,y in zip(r, c)) for c in bt] for r in a]

def chain_mul(mats):
    return reduce(matmul, mats)

A = [[1,2],[3,4]]
B = [[2,0],[1,2]]
C = [[0,1],[1,0]]
print(chain_mul([A,B,C]))

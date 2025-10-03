from collections import deque
def can_stack(cubes):
    dq = deque(cubes)
    l = float('inf')
    while dq:
        if dq[0] >= dq[-1] and dq[0] <= l:
            last = dq.popleft()
        elif dq[-1] >= dq[0] and dq[-1] <= l:
            last = dq.pop()
        else:
            return "No"
    return "Yes"
T = int(input())
for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    print(can_stack(blocks))

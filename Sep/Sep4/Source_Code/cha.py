from collections import defaultdict
grid=[[1,7,3],[9,8,2],[4,5,6]]
n = len(grid)
bottom_left_diags = defaultdict(list)
top_right_diags = defaultdict(list)

for i in range(n):
    for j in range(n):
        if i >= j:
            bottom_left_diags[i - j].append(grid[i][j])
        else:
            top_right_diags[i - j].append(grid[i][j])

for diag in bottom_left_diags.values():
    diag.sort(reverse=True)

for diag in top_right_diags.values():
    diag.sort()

for i in range(n):
    for j in range(n):
        if i >= j:
            grid[i][j] = bottom_left_diags[i - j].pop(0)
        else:
            grid[i][j] = top_right_diags[i - j].pop(0)
print(grid)
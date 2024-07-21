rects = [list(map(lambda x : int(x) + 1000, input().split())) for _ in range(3)]

grid = [[0 for _ in range(2000)] for _ in range(2000)]

for n, rect in enumerate(rects, start=1):
    x1, y1, x2, y2 = rect

    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = n

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1 or grid[i][j] == 2:
            res += 1

print(res)
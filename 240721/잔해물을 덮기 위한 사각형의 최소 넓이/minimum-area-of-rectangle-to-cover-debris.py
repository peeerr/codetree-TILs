rects = [list(map(lambda x : int(x) + 1000, input().split())) for _ in range(2)]

grid = [[0 for _ in range(2000)] for _ in range(2000)]

for n, rect in enumerate(rects, start=1):
    x1, y1, x2, y2 = rect

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = n

x1, y1, x2, y2 = 2000, 2000, 0, 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j] == 1:
            x1 = min(x1, i)
            y1 = min(y1, j)
            x2 = max(x2, i)
            y2 = max(y2, j)

res = 0
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        res += 1
print(res)
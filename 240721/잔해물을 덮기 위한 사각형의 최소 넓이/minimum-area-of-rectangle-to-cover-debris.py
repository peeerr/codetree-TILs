rects = [list(map(lambda x : int(x) + 1000, input().split())) for _ in range(2)]

grid = [[0 for _ in range(2000)] for _ in range(2000)]

for n, rect in enumerate(rects, start=1):
    x1, y1, x2, y2 = rect

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = n

x1, y1, x2, y2 = rects[0]
res_x = x1
res_y = []

for i in range(x1 + 1, x2):
    if 1 in grid[i]:
        res_x += 1
        tmp = y1
        for j in range(y1 + 1, y2):
            if grid[i][j] == 1 or grid[i][j] == 2:
                tmp += 1
        res_y.append(tmp)

res = 0
for i in range(x1, res_x + 1):
    for j in range(y1, max(res_y) + 1):
        res += 1

print(res)
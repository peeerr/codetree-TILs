rects = [list(map(lambda x : int(x) + 1000, input().split())) for _ in range(2)]

grid = [[0 for _ in range(2000)] for _ in range(2000)]

for n, rect in enumerate(rects, start=1):
    x1, y1, x2, y2 = rect

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = n

x1, y1, x2, y2 = rects[0]

x, y = 0, 0
cnt_x, cnt_y = 0, 0
for i in range(x1, x2):
    if 1 in grid[i] and cnt_x == 0:
        x1 = i
        cnt_x += 1
    for j in range(y1, y2):
        if grid[i][j] == 1 and cnt_y == 0:
            y1 = j
            cnt_y += 1
        if grid[i][j] == 1:
            x, y = i, j

res = 0
for i in range(x1, x + 1):
    for j in range(y1, y + 1):
        res += 1
print(res)
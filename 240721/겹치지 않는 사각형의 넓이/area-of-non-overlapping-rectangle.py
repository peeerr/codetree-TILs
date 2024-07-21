rects = [list(map(lambda x : int(x) + 1000, input().split())) for _ in range(3)]

grid = [[0 for _ in range(2000)] for _ in range(2000)]

for n in range(3):
    x1, y1, x2, y2 = rects[n]

    if n == 2:
        for i in range(y1, y2):
            for j in range(x1, x2):
                if grid[i][j] == 1:
                    grid[i][j] = 0
        break
        
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

res = 0
for x in grid:
    res += sum(x)

print(res)
n = int(input())

grid = [[0 for _ in range(100)] for _ in range(100)]
res = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(min(y1, y2), max(y1, y2)):
        for j in range(min(x1, x2), max(x1, x2)):
            grid[i][j] = 1

for x in grid:
    res += sum(x)

print(res)
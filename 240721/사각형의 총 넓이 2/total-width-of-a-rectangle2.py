n = int(input())

grid = [[0 for _ in range(200)] for _ in range(200)]
res = 0

for _ in range(n):
    x1, y1, x2, y2 = map(lambda x : int(x) + 100, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

for x in grid:
    res += sum(x)

print(res)
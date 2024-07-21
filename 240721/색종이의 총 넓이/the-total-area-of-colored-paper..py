n = int(input())

grid = [[0 for _ in range(200)] for _ in range(200)]

for _ in range(n):
    x, y = map(lambda x : int(x) + 100, input().split())

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            grid[i][j] = 1

res = 0
for x in grid:
    res += sum(x)

print(res)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

res = 0

for i in range(n):
    for j in range(n - 2):
        for k in range(i + 1, n):
            for l in range(n - 2):
                res = max(res, grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[k][l] + grid[k][l + 1] + grid[k][l + 2])

print(res)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

res = 0

for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                if i == k:
                    l = j + 3
                if l >= n - 2:
                    continue
                res = max(res, grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[k][l] + grid[k][l + 1] + grid[k][l + 2])

print(res)
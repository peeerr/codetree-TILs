def n_check(lst):
    global ans
    
    for i in range(2):
        for j in range(2):

            sum_n = 0
            for k in range(2):
                for l in range(2):
                    if k == i and l == j:
                        continue
                    sum_n += lst[k][l]

    ans = max(ans, sum_n)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n - 1):
    for j in range(m - 1):
        n_check([[grid[i][j], grid[i][j + 1]], [grid[i + 1][j], grid[i + 1][j + 1]]])

for i in range(n):
    for j in range(m):
        row, col = 0, 0
        if i + 2 < n:
            height = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
        if j + 2 < m:
            width = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        ans = max(ans, height, width)

print(ans)
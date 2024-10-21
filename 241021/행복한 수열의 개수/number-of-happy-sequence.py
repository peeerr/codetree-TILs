def is_happy(i, j):
    ret_Val = 0

    if i == 0:
        cnt = 1
        for k in range(i, n - 1):
            if grid[k][j] == grid[k + 1][j]:
                cnt += 1
            else:
                cnt = 1
        if cnt >= m:
            ret_Val += 1

    if j == 0:
        cnt = 1
        for k in range(j, n - 1):
            if grid[i][k] == grid[i][k + 1]:
                cnt += 1
            else:
                cnt = 1
        if cnt >= m:
            ret_Val += 1

    return ret_Val


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        ans += is_happy(i, j)

print(ans)
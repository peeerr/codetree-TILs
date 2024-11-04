def bomb():
    is_bomb = False

    for j in range(n):
        start, end = 0, 0
        cnt = 1

        for i in range(n):
            if i + 1 < n and grid[i][j] and grid[i][j] == grid[i + 1][j]:
                end = i + 1
                cnt += 1
            else:
                if cnt >= m:
                    is_bomb = True
                    for k in range(start, end + 1):
                        grid[k][j] = 0
                start, end = i + 1, i + 1
                cnt = 1

    return is_bomb


def drop():
    temp = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                temp[idx][j] = grid[i][j]
                idx -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def rotate():
    temp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for _ in range(k):
    while bomb():
        drop()
    rotate()
    drop()

for i in range(n):
    for j in range(n):
        if grid[i][j] > 0:
            ans += 1

print(ans)
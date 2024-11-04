def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bomb(c):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    x, y = -1, -1

    for r in range(n):
        if grid[r][c]:
            x, y = r, c
            break

    if not in_range(x, y):
        return

    for dx, dy in zip(dxs, dys):
        curr_x, curr_y = x, y
        for _ in range(grid[x][y] - 1):
            nx, ny = curr_x + dx, curr_y + dy

            if in_range(nx, ny):
                grid[nx][ny] = 0
                curr_x, curr_y = nx, ny
    grid[x][y] = 0


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


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cols = list(map(lambda x : x - 1, [int(input()) for _ in range(m)]))

for col in cols:
    bomb(1)
    drop()

for i in range(n):
    print(*grid[i])
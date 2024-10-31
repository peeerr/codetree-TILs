def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def cut(x, y):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):

        curr_x, curr_y = x, y
        for _ in range(grid[x][y] - 1):
            nx, ny = curr_x + dx, curr_y + dy

            if in_range(nx, ny):
                curr_x, curr_y = nx, ny
                grid[nx][ny] = 0

    grid[x][y] = 0


def fall():
    for i in range(n):
        temp = [0 for _ in range(n)]
        idx = 0

        for j in range(n - 1, -1, -1):
            if grid[j][i]:
                temp[idx] = grid[j][i]
                idx += 1

        for j in range(n - 1, -1, -1):
            grid[j][i] = temp[n - j - 1]


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
x, y = map(lambda x : int(x) - 1, input().split())

cut(x, y)
fall()

for i in range(n):
    print(*grid[i])
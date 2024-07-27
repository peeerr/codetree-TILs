def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, m = map(int, input().split())

grid = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

for _ in range(m):
    x, y = map(lambda x : int(x) - 1, input().split())
    grid[x][y] = 1
    cnt = 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)
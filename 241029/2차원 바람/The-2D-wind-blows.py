def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def rotation(x1, y1, x2, y2):
    temp1 = grid[x1][y2]
    temp2 = grid[x2][y2]
    temp3 = grid[x2][y1]

    for y in range(y2, y1, -1):
        grid[x1][y] = grid[x1][y - 1]

    for x in range(x2, x1 + 1, -1):
        grid[x][y2] = grid[x - 1][y2]
    grid[x1 + 1][y2] = temp1

    for y in range(y1, y2):
        grid[x2][y] = grid[x2][y + 1]
    grid[x2][y2 - 1] = temp2

    for x in range(x1, x2 - 1):
        grid[x][y1] = grid[x + 1][y1]
    grid[x2 - 1][y1] = temp3


def replace_to_average(x1, y1, x2, y2):
    temp = [[-1 for _ in range(m)] for _ in range(n)]
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            total = grid[x][y]
            cnt = 1

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    total += grid[nx][ny]
                    cnt += 1
            
            temp[x][y] = total // cnt

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = temp[x][y]


n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
positions = [list(map(lambda x : int(x) - 1, input().split())) for _ in range(q)]

for x1, y1, x2, y2 in positions:
    rotation(x1, y1, x2, y2)
    replace_to_average(x1, y1, x2, y2)

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
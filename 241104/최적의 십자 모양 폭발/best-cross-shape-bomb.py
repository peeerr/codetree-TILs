def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def in_bomb_range(x1, y1, x2, y2):
    return 0 <= x2 < n and 0 <= y2 < n and (abs(x1 - x2) < grid[x1][y1] and y1 == y2) or (
                abs(y1 - y2) < grid[x1][y1] and x1 == x2)


def bomb(x, y):
    next_grid = [[0 for _ in range(n)] for _ in range(n)]
    temp = [[grid[i][j] for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if in_bomb_range(x, y, i, j):
                temp[i][j] = 0

    for j in range(n):
        idx = 0
        for i in range(n - 1, -1, -1):
            if temp[i][j]:
                next_grid[idx][j] = temp[i][j]
                idx += 1

    return get_pair_cnt(next_grid)


def get_pair_cnt(next_grid):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    cnt = 0

    for x in range(n):
        for y in range(n):
            if next_grid[x][y]:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and next_grid[nx][ny] == next_grid[x][y]:
                        cnt += 1

    return cnt // 2


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, bomb(i, j))

print(ans)
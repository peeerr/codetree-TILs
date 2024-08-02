def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
res = 0

for x in range(n):
    for y in range(m):
        if grid[x][y] == 'L':
            for dx, dy in zip(dxs, dys):
                nx1, ny1 = x + dx, y + dy
                nx2, ny2 = y + (dy * 2), y + (dy * 2)
                if in_range(nx1, ny1) and in_range(nx2, ny2) and grid[nx1][ny1] == 'E' and grid[nx2][ny2] == 'E':
                    res += 1

print(res)
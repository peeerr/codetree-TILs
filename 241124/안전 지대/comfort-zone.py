def in_range(x, y):
    return 0 <= x < n and 0 <= y < m and next_grid[x][y]


def dfs(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy 

        if in_range(nx, ny):
            next_grid[nx][ny] = 0
            dfs(nx, ny)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_area = 0
ans = 101

for k in range(101):
    next_grid = [[1 for _ in range(m)] for _ in range(n)]
    area = 0
    
    for x in range(n):
        for y in range(m):
            if grid[x][y] <= k:
                next_grid[x][y] = 0

    for x in range(n):
        for y in range(m):
            if next_grid[x][y]:
                area += 1
                dfs(x, y)

    if max_area < area:
        max_area = area
        ans = k

print(max_area, ans)

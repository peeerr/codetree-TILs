def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and next_grid[x][y] and not visited[x][y]


def dfs(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy 

            if can_go(nx, ny):
                visited[nx][ny] = True
                stack.append((nx, ny))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_area = 0
ans = 101

for k in range(1, 101):
    next_grid = [[1 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    area = 0
    
    for x in range(n):
        for y in range(m):
            if grid[x][y] <= k:
                next_grid[x][y] = 0

    for x in range(n):
        for y in range(m):
            if can_go(x, y):
                area += 1
                visited[x][y] = True
                dfs(x, y)

    if max_area < area:
        max_area = area
        ans = k
    elif max_area == area:
        ans = min(ans, k)

print(ans, max_area)

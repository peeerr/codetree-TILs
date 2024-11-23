def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y]


def dfs(x, y):
    global ans

    if x == n - 1 and y == m - 1:
        ans = 1

    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
ans = 0

visited[0][0] = True
dfs(0, 0)

print(ans)

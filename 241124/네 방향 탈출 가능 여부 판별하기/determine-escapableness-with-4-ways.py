from collections import deque


def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and grid[x][y] and not visited[x][y]


def bfs(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
bfs(0, 0)

print(visited[n - 1][m - 1])

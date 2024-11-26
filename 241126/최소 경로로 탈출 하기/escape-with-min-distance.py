from collections import deque


def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y]


def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                step[nx][ny] = step[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

step = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = True

bfs()
ans = step[n - 1][m - 1]

print(ans if ans else -1)

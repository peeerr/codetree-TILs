from collections import deque


def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and not grid[x][y]


def bfs(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy 

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
positions = [tuple(map(lambda x : int(x) - 1, input().split())) for _ in range(k)]

visited = [[False for _ in range(n)] for _ in range(n)]

for x, y in positions:
    visited[x][y] = True
    bfs(x, y)

print(sum([1 for y in range(n) for x in range(n) if visited[x][y]]))

from collections import deque


def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and grid[x][y] == 1


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


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]
q = deque()

for x in range(n):
    for y in range(n):
        if grid[x][y] == 2:
            visited[x][y] = True 
            q.append((x, y))
            
bfs()

for x in range(n):
    for y in range(n):
        if not grid[x][y]:
            step[x][y] = -1
        elif grid[x][y] == 1 and step[x][y] == 0:
            step[x][y] = -2

for x in range(n):
    print(*step[x])

from collections import deque


def have_effect():
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and visited[i][j]:
                return True
    return False


def record(visited):
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                water_have_effect[i][j] = True

def init():
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                water_have_effect[i][j] = True


def melt():
    global cnt
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for x in range(n):
        for y in range(m):
            if water_have_effect[x][y]:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and grid[nx][ny]:
                        cnt += 1
                        grid[nx][ny] = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and not grid[x][y]


def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))


def is_all_melted():
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                return False
    return True


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

time = 0
last_melted = 0

for t in range(1, max(n, m)):
    water_have_effect = [[False for _ in range(m)] for _ in range(n)]
    init()

    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1 or grid[i][j]:
                continue
            
            visited = [[False for _ in range(m)] for _ in range(n)]
            visited[i][j] = True
            q = deque([(i, j)])
            bfs()
            
            if have_effect():
                record(visited)
                
    cnt = 0
    melt()

    if is_all_melted():
        time = t
        last_melted = cnt
        break

print(time, last_melted)

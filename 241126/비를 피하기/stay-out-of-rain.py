from collections import deque


def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and grid[x][y] != 1


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
        

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)] 

positions = [(x, y) for x in range(n) for y in range(n) if grid[x][y] == 3]
step = [[0 for _ in range(n)] for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()

for x, y in positions:
    q.append((x, y))    

bfs()

ans = [[0 for _ in range(n)] for _ in range(n)]

for x in range(n):
    for y in range(n):
        if grid[x][y] == 2:
            if step[x][y]:
                ans[x][y] = step[x][y]
            else:
                ans[x][y] = -1

for i in range(n):
    print(*ans[i])

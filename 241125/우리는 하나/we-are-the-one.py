from itertools import combinations
from collections import deque


def init():
    for i in range(n):
        for j in range(n):
            positions.append((i, j))


def can_go(x, y, num):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and u <= abs(grid[x][y] - num) <= d


def bfs():
    global cnt
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny, grid[x][y]):
                cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))


n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

positions = []
init()

ans = 0

for pos in combinations(positions, k):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = k

    for x, y in pos:
        q = deque([(x, y)])
        visited[x][y] = True
        bfs()

    ans = max(ans, cnt)

print(ans)

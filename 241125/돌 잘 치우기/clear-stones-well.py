from itertools import combinations
from collections import deque


def get_all_stones_pos():
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                stones.append((i, j))


def init_temp():
    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[i][j]


def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and not temp[x][y]


def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))


n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
positions = [tuple(map(lambda x : int(x) - 1, input().split())) for _ in range(k)]

stones = []
temp = [[0 for _ in range(n)] for _ in range(n)]
get_all_stones_pos()

ans = 0

for stone_positions in combinations(stones, m):
    init_temp()
    visited = [[False for _ in range(n)] for _ in range(n)]

    for x, y in stone_positions:
        temp[x][y] = 0

    for x, y in positions:
        q = deque([(x, y)])
        visited[x][y] = True
        bfs()

    ans = max(ans, sum([1 for j in range(n) for i in range(n) if visited[i][j]]))

print(ans)

import sys
from itertools import combinations
from collections import deque


def find_all_walls():
    walls_pos = []
    for x in range(n):
        for y in range(n):
            if grid[x][y]:
                walls_pos.append((x, y))
    return walls_pos


def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and not temp[x][y]


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

                if (nx, ny) == (end_x, end_y):
                    return


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = map(lambda x: int(x) - 1, input().split())
end_x, end_y = map(lambda x: int(x) - 1, input().split())

ans = sys.maxsize

walls_pos = find_all_walls()
temp = [[0 for _ in range(n)] for _ in range(n)]

for comb in combinations(walls_pos, k):
    step = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            temp[x][y] = grid[x][y]

    for x, y in comb:
        temp[x][y] = 0

    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    bfs()

    if visited[end_x][end_y]:
        ans = min(ans, step[end_x][end_y])

print(ans if ans != sys.maxsize else -1)

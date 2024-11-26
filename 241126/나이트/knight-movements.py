from collections import deque


def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]


def bfs():
    dxs, dys = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                step[nx][ny] = step[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))


n = int(input())
start_x, start_y, end_x, end_y = map(lambda x : int(x) - 1, input().split())

step = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

q = deque([(start_x, start_y)])
visited[start_x][start_y] = True

bfs()

if visited[end_x][end_y]:
    print(step[end_x][end_y])
else:
    print(-1)

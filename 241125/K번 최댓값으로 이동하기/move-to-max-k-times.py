from collections import deque


def can_go(x, y, num):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and grid[x][y] < num


def bfs(num):
    global is_go

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_num = 0
    max_x, max_y = n, n

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny, num):
                is_go = True
                visited[nx][ny] = True
                q.append((nx, ny))
                
                if (grid[nx][ny], -nx, -ny) > (max_num, -max_x, -max_y):
                    max_num = grid[nx][ny]
                    max_x, max_y = nx, ny

    return max_x, max_y


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
x, y = map(lambda x : int(x) - 1, input().split())

for _ in range(k):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque([(x, y)])

    is_go = False
    visited[x][y] = True
    max_x, max_y = bfs(grid[x][y])

    if is_go:
        x, y = max_x, max_y
    else:
        break

print(x + 1, y + 1)

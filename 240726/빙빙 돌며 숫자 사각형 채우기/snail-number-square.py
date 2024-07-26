def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
grid = [[0 for _ in range(m)] for _ in range(n)]

direction = 0
x, y = 0, 0

for i in range(1, n * m + 1):
    grid[x][y] = i
    nx, ny = x + dx[direction], y + dy[direction]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        direction = (direction + 1) % 4

    x, y = x + dx[direction], y + dy[direction]

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
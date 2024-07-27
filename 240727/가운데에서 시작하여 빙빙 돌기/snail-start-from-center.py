def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())

grid = [[0 for _ in range(n)] for _ in range(n)]

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
x, y = n - 1, n - 1
direction = 0

for num in range(n ** 2, 0, -1):
    grid[x][y] = num

    nx, ny = x + dx[direction], y + dy[direction]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        direction = (direction + 1) % 4

    x, y = x + dx[direction], y + dy[direction]

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
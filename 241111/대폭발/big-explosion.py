def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, m, r, c = map(int, input().split())
r, c = r - 1, c - 1

grid = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

grid[r][c] = 1

for t in range(1, m + 1):
    distance = 2 ** (t - 1)
    positions = []

    for x in range(n):
        for y in range(n):

            if not grid[x][y]:
                continue

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx * distance, y + dy * distance

                if in_range(nx, ny):
                    positions.append((nx, ny))

    for pos in positions:
        x, y = pos
        grid[x][y] = 1

print(sum([grid[i][j] for j in range(n) for i in range(n)]))
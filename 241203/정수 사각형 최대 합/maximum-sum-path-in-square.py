def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

d = [[0 for _ in range(n)] for _ in range(n)]

dxs, dys = [0, -1], [-1, 0]

for x in range(n):
    for y in range(n):
        max_x, max_y, max_num = -1, -1, 0
        for dx, dy in zip(dxs, dys):
            prev_x, prev_y = x + dx, y + dy
            if in_range(prev_x, prev_y) and d[prev_x][prev_y] > max_num:
                max_x, max_y, max_num = prev_x, prev_y, d[prev_x][prev_y]
        if max_x != -1 and max_y != -1:
            d[x][y] = grid[x][y] + d[max_x][max_y]
        else:
            d[x][y] = grid[x][y]

print(d[n - 1][n - 1])

MAX_INT = 1000001

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

d = [[0 for _ in range(n)] for _ in range(n)]

dxs, dys = [0, -1], [-1, 0]

for x in range(n):
    for y in range(n):
        min_x, min_y, min_num = -1, -1, MAX_INT
        for dx, dy in zip(dxs, dys):
            prev_x, prev_y = x + dx, y + dy
            if in_range(prev_x, prev_y) and d[prev_x][prev_y] < min_num:
                min_x, min_y, min_num = prev_x, prev_y, d[prev_x][prev_y]
        if min_x != -1 and min_y != -1:
            d[x][y] = max(grid[x][y], d[min_x][min_y])
        else:
            d[x][y] = grid[x][y]

print(d[n - 1][n - 1])

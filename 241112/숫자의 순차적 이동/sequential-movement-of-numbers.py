def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def simulate(num):
    for x in range(n):
        for y in range(n):
            if grid[x][y] != num:
                continue

            max_num, max_x, max_y = 0, 0, 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy

                if in_range(nx, ny) and grid[nx][ny] > max_num:
                    max_num = grid[nx][ny]
                    max_x, max_y = nx, ny
            
            grid[x][y], grid[max_x][max_y] = grid[max_x][max_y], grid[x][y]  
            return


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    num = 1
    while num != n * n + 1:
        simulate(num)
        num += 1

for i in range(n):
    print(*grid[i])

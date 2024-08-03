def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n = 19
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

res = 0
pos = (0, 0)

for x in range(n):
    for y in range(n):
        if grid[x][y] != 0:
            for dx, dy in zip(dxs, dys):
                cnt = 0
                for i in range(1, 5):
                    nx, ny = x + (dx * i), y + (dy * i)
                    if in_range(nx, ny) and grid[nx][ny] == grid[x][y]:
                        cnt += 1
                        if i == 2:
                            tmp = (nx + 1, ny + 1)        
                if cnt == 4:
                    res = grid[x][y]
                    pos = tmp

print(res)

if res != 0:
    print(*pos)
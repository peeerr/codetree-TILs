def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, x, y = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
x, y = x - 1, y - 1
ans = [grid[x][y]]

while True:
    length = len(ans)

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[x][y] < grid[nx][ny]:
            ans.append(grid[nx][ny])
            x, y = nx, ny
    
    if length == len(ans):
        break

print(*ans)
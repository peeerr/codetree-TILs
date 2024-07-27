def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n, t = map(int, input().split())
insts = list(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
direction = 0
x, y = n // 2, n // 2
ans = grid[x][y]

for inst in insts:
    if inst == 'R':
        direction = (direction + 1) % 4
    elif inst == 'L':
        direction = (direction + 3) % 4
    else:
        nx, ny = x + dx[direction], y + dy[direction]
        if in_range(nx, ny):
            x, y = nx, ny
            ans += grid[x][y]

print(ans)
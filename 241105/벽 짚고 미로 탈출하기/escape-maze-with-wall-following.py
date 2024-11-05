def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())
x, y = map(lambda x : int(x) - 1, input().split())
maze = [list(input()) for _ in range(n)]

start_x, start_y = x, y

counterclock_dxs, counterclock_dys = [0, -1, 0, 1], [1, 0, -1, 0]
clock_dxs, clock_dys = [0, 1, 0, -1], [1, 0, -1, 0]

is_out = True
ans = 0
d = 0
clockwise = True
cnt = 0

while True:
    if cnt == 4:
        is_out = False
        break

    if clockwise:
        nx, ny = x + clock_dxs[d], y + clock_dys[d]
    else:
        nx, ny = x + counterclock_dxs[d], y + counterclock_dys[d]

    if not in_range(nx, ny):
        ans += 1
        break

    if maze[nx][ny] == '#':
        if clockwise:
            cnt = 0
            clockwise = False
            d = (d - 1) + 4 % 4
        else:
            cnt += 1
            d = (d + 1) % 4
        continue
    else:
        if not clockwise and d == 1:
            d += 2
            clockwise = True
        elif not clockwise and d == 3:
            d -= 2
            clockwise = True
        else:
            nnx, nny = nx + clock_dxs[(d + 1) % 4], ny + clock_dys[(d + 1) % 4]
            if not in_range(nnx, nny) or maze[nnx][nny] == '.':
                d = (d + 1) % 4
            x, y = nx, ny
            ans += 1
            clockwise = True

    if x == start_x and y == start_y:
        is_out = False
        break

print(ans) if is_out else print(-1)
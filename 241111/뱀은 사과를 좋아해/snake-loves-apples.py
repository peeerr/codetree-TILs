def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n, m, k = map(int, input().split())

positions = [tuple(map(lambda x : int(x) - 1, input().split())) for _ in range(m)]
moves = [tuple(map(lambda x : int(x) if x.isdigit() else x, input().split())) for _ in range(k)]
grid = [[0 for _ in range(n)] for _ in range(n)]

for x, y in positions:
    grid[x][y] = 1

dxs_dir, dys_dir = {'U': -1, 'R': 0, 'D': 1, 'L': 0}, {'U': 0, 'R': 1, 'D': 0, 'L': -1}
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = 0, 0

# 2는 뱀을 표현
grid[x][y] = 2

tail_x, tail_y = x, y
ans = 0
is_done = False

for d, p in moves:
    for _ in range(p):
        ans += 1
        nx, ny = x + dxs_dir[d], y + dys_dir[d]

        if not in_range(nx, ny):
            is_done = True
            break

        # 이동할 위치에 사과가 없다면, 꼬리 위치 조정
        if grid[nx][ny] == 0 or grid[nx][ny] == 2:
            grid[tail_x][tail_y] = 0
            is_move = False

            for dx, dy in zip(dxs, dys):
                tail_nx, tail_ny = tail_x + dx, tail_y + dy

                if in_range(tail_nx, tail_ny) and grid[tail_nx][tail_ny] == 2:
                    tail_x, tail_y = tail_nx, tail_ny
                    is_move = True
                    break
            
            if not is_move:
                tail_x, tail_y = nx, ny

        # 겹친 경우 종료
        if grid[nx][ny] == 2:
            is_done = True
            break

        # 이동
        x, y = nx, ny
        grid[x][y] = 2

    if is_done:
        break

print(ans)
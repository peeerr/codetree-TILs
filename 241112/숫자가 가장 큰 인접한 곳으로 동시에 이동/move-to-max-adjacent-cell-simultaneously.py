def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
positions = [tuple(map(lambda x : int(x) - 1, input().split())) for _ in range(m)]
 
count = [[0 for _ in range(n)] for _ in range(n)]
next_pos = []

for x, y in positions:
    count[x][y] += 1
    next_pos.append((x, y))

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

for _ in range(t):
    temp = []

    for x, y in next_pos:
        if not count[x][y]:
            continue
        
        max_num = 0
        max_x, max_y = x, y
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and grid[nx][ny] > max_num:
                max_num = grid[nx][ny]
                max_x, max_y = nx, ny

        count[max_x][max_y] += 1
        count[x][y] -= 1
        temp.append((max_x, max_y))

    next_pos = [x for x in temp]

    # for x in range(n):
    #     for y in range(n):
    #         if count[x][y] > 1:
    #             count[x][y] = 0

print(sum([1 if count[x][y] == 1 else 0 for y in range(n) for x in range(n)]))

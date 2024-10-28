def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def rectangle_sum(x, y):
    global ans

    for i in range(1, n):
        for j in range(1, n):
            total = 0
            is_move_0, is_move_2 = False, False 
            is_move_1, is_move_3 = False, False 

            for k in range(len(dxs)):
                if k == 0 or k == 2:
                    for _ in range(i):
                        nx, ny = x + dxs[k], y + dys[k]
                        if not in_range(nx, ny):
                            break
                        if k == 0:
                            is_move_0 = True
                        if k == 2:
                            is_move_2 = True
                        total += grid[x][y]
                        x, y = nx, ny

                elif k == 1 or k == 3:
                    for _ in range(j):
                        nx, ny = x + dxs[k], y + dys[k]
                        if not in_range(nx, ny):
                            break
                        if k == 1:
                            is_move_1 = True
                        if k == 3:
                            is_move_3 = True
                        total += grid[x][y]
                        x, y = nx, ny

            if is_move_0 and is_move_1 and is_move_2 and is_move_3:
                ans = max(ans, total)


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
ans = 0

for x in range(2, n):
    for y in range(1, n - 1):
        rectangle_sum(x, y)

print(ans)
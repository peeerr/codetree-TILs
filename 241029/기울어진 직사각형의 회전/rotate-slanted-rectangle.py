def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def move(d):
    global x, y, direction
    dxs, dys = ([-1, -1, 1, 1], [1, -1, -1, 1]) if direction else ([-1, -1, 1, 1], [-1, 1, 1, -1])

    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx, ny):
        grid[x][y] = grid[nx][ny]
        x, y = nx, ny


def rotate(m1, m2, m3, m4):
    global x, y, direction
    temp = grid[x][y]

    if direction:
        move_nums = [m1, m2, m3, m4]
    else:
        move_nums = [m4, m3, m2, m1]

    for i, move_num in enumerate(move_nums):
        for _ in range(move_num):
            move(i)
    
    if direction:
        grid[x - 1][y - 1] = temp
    else:
        grid[x - 1][y + 1] = temp


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
x, y, m1, m2, m3, m4, direction = map(int, input().split())
x, y = x - 1, y - 1

rotate(m1, m2, m3, m4)

for i in range(n):
    print(*grid[i])
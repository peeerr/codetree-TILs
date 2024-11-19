def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def max_bomb(selected_shapes):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    dxs, dys = {'U': -1, 'D': 1, 'L': 0, 'R': 0, 'UL': -1, 'UR': -1, 'DL': 1, 'DR': 1}, {'U': 0, 'D': 0, 'L': -1, 'R': 1, 'UL': -1, 'UR': 1, 'DL': -1, 'DR': 1}
    shapes = [{'U': 2, 'D': 2}, {'U': 1, 'D': 1, 'L': 1, 'R': 1}, {'UL': 1, 'UR': 1, 'DL': 1, 'DR': 1}]
    
    for i, (x, y) in zip(selected_shapes, bomb_pos):
        grid[x][y] = 1
        shape = shapes[i]

        for d, iter_num in shape.items():
            curr_x, curr_y = x, y 
            for _ in range(iter_num):
                nx, ny = curr_x + dxs[d], curr_y + dys[d]

                if in_range(nx, ny):
                    curr_x, curr_y = nx, ny
                    grid[nx][ny] = 1

    return sum([1 for j in range(n) for i in range(n) if grid[i][j]])


def f(k):
    global ans

    if k == 0:
        ans = max(ans, max_bomb(selected_shapes))
        return

    for i in range(3):
        selected_shapes.append(i)
        f(k - 1)
        selected_shapes.pop()


n = int(input())
bomb = [list(map(int, input().split())) for _ in range(n)]
bomb_pos = []
selected_shapes = []

for i in range(n):
    for j in range(n):
        if bomb[i][j]:
            bomb_pos.append((i, j))

ans = 0
f(len(bomb_pos))
print(ans)

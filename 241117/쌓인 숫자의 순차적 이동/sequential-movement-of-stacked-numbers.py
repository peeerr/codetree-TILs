from collections import deque


def can_move(x, y):
    return 0 <= x < n and 0 <= y < n and len(grid[x][y])


def find_pos(num):
    for x in range(n):
        for y in range(n):
            if num in grid[x][y]:
                return x, y, grid[x][y].index(num)


def find_max_num_pos(x, y):
    dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    max_num, max_x, max_y = 0, -1, -1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
    
        if can_move(nx, ny) and max(grid[nx][ny]) > max_num:
            max_num, max_x, max_y = max(grid[nx][ny]), nx, ny

    return max_x, max_y


def move(x, y, idx):
    max_x, max_y = find_max_num_pos(x, y)

    # 갈 곳이 없다면
    if max_x == -1 and max_y == -1:
        return

    move_nums = deque()
    for i in range(idx + 1):
        move_nums.appendleft(grid[x][y].popleft())

    grid[max_x][max_y].extendleft(move_nums)


def simulate(num):
    x, y, idx = find_pos(num)
    move(x, y, idx)


n, m = map(int, input().split())
grid = [list(map(lambda x : deque([int(x)]), input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))

for num in move_nums:
    simulate(num)

for x in range(n):
    for y in range(n):
        if not len(grid[x][y]):
            print(None)
        else:
            print(*grid[x][y])

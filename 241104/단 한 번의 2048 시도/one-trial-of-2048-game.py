def left_push():
    for x in range(n):
        temp = [0 for _ in range(n)]
        is_already = False
        idx = 0

        for y in range(n):
            if grid[x][y]:
                if not is_already and idx - 1 >= 0 and temp[idx - 1] == grid[x][y]:
                    temp[idx - 1] += grid[x][y]
                    is_already = True
                else:
                    temp[idx] = grid[x][y]
                    is_already = False
                    idx += 1

        for i in range(n):
            grid[x][i] = temp[i]


def right_push():
    for x in range(n):
        temp = [0 for _ in range(n)]
        is_already = False
        idx = 3

        for y in range(n - 1, -1, -1):
            if grid[x][y]:
                if not is_already and idx + 1 < n and temp[idx + 1] == grid[x][y]:
                    temp[idx + 1] += grid[x][y]
                    is_already = True
                else:
                    temp[idx] = grid[x][y]
                    is_already = False
                    idx -= 1

        for i in range(n):
            grid[x][i] = temp[i]


def up_push():
    for y in range(n):
        temp = [0 for _ in range(n)]
        is_already = False
        idx = 0

        for x in range(n):
            if grid[x][y]:
                if not is_already and idx - 1 >= 0 and temp[idx - 1] == grid[x][y]:
                    temp[idx - 1] += grid[x][y]
                    is_already = True
                else:
                    temp[idx] = grid[x][y]
                    is_already = False
                    idx += 1

        for i in range(n):
            grid[i][y] = temp[i]


def down_push():
    for y in range(n):
        temp = [0 for _ in range(n)]
        is_already = False
        idx = 3

        for x in range(n - 1, -1, -1):
            if grid[x][y]:
                if not is_already and idx + 1 < n and temp[idx + 1] == grid[x][y]:
                    temp[idx + 1] += grid[x][y]
                    is_already = True
                else:
                    temp[idx] = grid[x][y]
                    is_already = False
                    idx -= 1

        for i in range(n):
            grid[i][y] = temp[i]


n = 4
grid = [list(map(int, input().split())) for _ in range(n)]
d = input()

if d == 'L':
    left_push()
elif d == 'R':
    right_push()
elif d == 'U':
    up_push()
elif d == 'D':
    down_push()

for i in range(n):
    print(*grid[i])
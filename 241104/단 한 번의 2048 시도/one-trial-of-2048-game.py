def rotate():
    temp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def move():
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
    for _ in range(3):
        rotate()
    move()
    rotate()
elif d == 'R':
    rotate()
    move()
    for _ in range(3):
        rotate()
elif d == 'U':
    rotate(); rotate()
    move()
    rotate(); rotate()
elif d == 'D':
    move()

for i in range(n):
    print(*grid[i])
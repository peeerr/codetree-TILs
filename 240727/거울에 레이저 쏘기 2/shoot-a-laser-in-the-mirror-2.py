def init(n):
    x, y = 0, 0
    direction = 0
    cnt = 0
    finish = 0
    for i in range(4):
        if i == 0 or i == 1:
            for j in range(n):
                if i == 0:
                    x, y = x, j
                    direction = 2
                elif i == 1:
                    x, y = j, y
                    direction = 3
                cnt += 1
                if cnt == k:
                    finish = 1
                    break
                
        elif i == 2 or i == 3:
            for a in range(n - 1, -1, -1):
                if i == 2:
                    x, y = x, a
                    direction = 0
                elif i == 3:
                    x, y = a, y
                    direction = 1
                cnt += 1
                if cnt == k:
                    finish = 1
                    break
        if finish == 1:
            break
    return x, y, direction


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y, direction = init(n)
# print(x, y)
# print(direction)

cnt = 1
end = False

while True:
    if grid[x][y] == '/':
        if direction == 0:
            direction += 1
        elif direction == 1:
            direction -= 1
        elif direction == 2:
            direction += 1
        else:
            direction -= 1
        nx, ny = x + dx[direction], y + dy[direction]
        if in_range(nx, ny):
            cnt += 1
            x, y = nx, ny
        else:
            break
    else:
        if direction == 0:
            direction = 3
        elif direction == 1:
            direction = 2
        elif direction == 2:
            direction = 1
        else:
            direction = 0
        nx, ny = x + dx[direction], y + dy[direction]
        if in_range(nx, ny):
            cnt += 1
            x, y = nx, ny
        else:
            break

print(cnt)
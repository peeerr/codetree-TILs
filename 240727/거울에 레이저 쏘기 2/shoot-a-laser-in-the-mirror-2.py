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

cnt = 0
end = False

while in_range(x, y):
    if grid[x][y] == '/':
        direction = direction ^ 1
        x, y = x + dx[direction], y + dy[direction]
    else:
        direction = 3 - direction
        x, y = x + dx[direction], y + dy[direction]
    cnt += 1

print(cnt)
def init_direction(x, y):
    if x == 0 and y == 0:
        return [0, 3]
    elif x == 0 and y == n - 1:
        return [2, 3]
    elif x == n - 1 and y == 0:
        return [0, 1]
    elif x == n - 1 and y == n - 1:
        return [2, 3]
    elif x == 0 and 0 < y < n - 1:
        return [3]
    elif x == n - 1 and 0 < y < n - 1:
        return [1]
    elif 0 < x < n - 1 and y == 0:
        return [0]
    elif 0 < x < n - 1 and y == n - 1:
        return [2]
    else:
        return []


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def simulate(x, y, d):
    global ans
    cnt = 1

    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

    while in_range(x, y):
        if grid[x][y] == 1:
            d ^= 1
        elif grid[x][y] == 2:
            if d % 2 == 0:
                d = (d - 1 + 4) % 4
            else:
                d = (d + 1) % 4
        x, y = x + dxs[d], y + dys[d]
        cnt += 1

    ans = max(ans, cnt)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for x in range(n):
    for y in range(n):
        for d in init_direction(x, y):
            simulate(x, y, d)

print(ans)

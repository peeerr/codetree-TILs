def init(k, n):
    if k <= n:
        return 0, k - 1, 2
    elif k <= 2 * n:
        return k - n - 1, n - 1, 3
    elif k <= 3 * n:
        return n - 1, (k - n  - 1) % n, 0
    else:
        return n - (k - 1) % n - 1, 0, 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y, direction = init(k, n)

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
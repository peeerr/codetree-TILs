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
            d = 3 - d
        x, y = x + dxs[d], y + dys[d]
        cnt += 1

    ans = max(ans, cnt)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    simulate(0, i, 3)
    simulate(i, 0, 0)
    simulate(i, n - 1, 2)
    simulate(n - 1, i, 1)

print(ans)

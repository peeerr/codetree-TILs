def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def rectangle_sum(x, y, i, j):
    total = 0
    move_nums = [i, j, i, j]

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                return 0
            
            total += grid[nx][ny]
            x, y = nx, ny

    return total


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
ans = 0

for x in range(2, n):
    for y in range(1, n - 1):
        for i in range(1, n):
            for j in range(1, n):
               ans = max(ans, rectangle_sum(x, y, i, j))

print(ans)
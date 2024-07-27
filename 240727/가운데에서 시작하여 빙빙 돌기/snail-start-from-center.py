def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())

grid = [[0 for _ in range(n)] for _ in range(n)]

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
x, y = n // 2, n // 2
direction, distance = 0, 0
end = False

num = 1
while True:
    if direction == 0 or direction == 2:
        distance += 1

    for _ in range(distance):
        grid[x][y] = num
        num += 1
        x, y = x + dx[direction], y + dy[direction]

        if not in_range(x, y):
            end = True
            break

    if end:
        break
    direction = (direction + 1) % 4

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
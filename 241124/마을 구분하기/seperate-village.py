def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and grid[x][y]


def dfs(x, y):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            grid[nx][ny] = 0
            temp.append(1)
            dfs(nx, ny)


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

villages = 0
people = []

for x in range(n):
    for y in range(n):
        if grid[x][y]:
            grid[x][y] = 0
            villages += 1
            temp = [1]
            dfs(x, y)
            people.append(sum(temp))

print(villages)
for x in sorted(people):
    print(x)

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]


def dfs(x, y):
    global block_num
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny) and grid[x][y] == grid[nx][ny]:
            block_num += 1
            visited[nx][ny] = True
            dfs(nx, ny)


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
bomb_num, max_block_num = 0, 0

for x in range(n):
    for y in range(n):
        if can_go(x, y):
            block_num = 1

            visited[x][y] = True
            dfs(x, y)

            if block_num >= 4:
                bomb_num += 1
            max_block_num = max(max_block_num, block_num)

print(bomb_num, max_block_num)

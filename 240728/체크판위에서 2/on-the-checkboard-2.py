r, c = map(int, input().split())
grid = [input().split() for _ in range(r)]

ans = 0

for i in range(1, r):
    for j in range(1, c):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                if grid[0][0] != grid[i][j] and grid[i][j] != grid[k][l] and grid[k][l] != grid[r - 1][c - 1]:
                    ans += 1

print(ans)
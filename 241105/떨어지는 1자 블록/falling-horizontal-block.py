n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
k -= 1

for i in range(n):
    can_down = True

    for j in range(k, k + m):
        if i + 1 < n and grid[i + 1][j]:
            can_down = False
    
    if not can_down:
        for j in range(k, k + m):
            grid[i][j] = 1
        break
    
    if i + 1 == n:
        for j in range(k, k + m):
            grid[i][j] = 1

for i in range(n):
    print(*grid[i])
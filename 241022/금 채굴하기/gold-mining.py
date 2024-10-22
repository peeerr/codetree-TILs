def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for k in range(n):
    
    for i in range(n):
        for j in range(n):

            if k == 0:
                ans = max(ans, grid[i][j])
                continue

            cost, gold = 0, 0

            for l in range(i - k + 1, i + k):
                for o in range(j - k + 1, j + k):
                    cost += 1
                    if not in_range(l, o):
                        continue
                    gold += grid[l][o]
                    if i == 1 and j == 1 and k == 0:
                        test[l][o] += grid[l][o]
            
            if in_range(i - k, j):
                gold += grid[i - k][j]
            if in_range(i + k, j):
                gold += grid[i + k][j]
            if in_range(i, j - k):
                gold += grid[i][j - k]
            if in_range(i, j + k):
                gold += grid[i][j + k]
            cost += 4

            if cost <= m * gold:
                ans = max(ans, gold)

print(ans)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for k in range(n + 1):
    
    for i in range(n):
        for j in range(n):
            
            cost, gold = 0, 0

            for l in range(-25, 25):
                for o in range(-25, 25):
                    if abs(l - i) + abs(o - j) <= k:
                        cost += 1
                        if in_range(l, o):
                            gold += grid[l][o]

            if cost <= m * gold:
                ans = max(ans, gold)

print(ans)
import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = -sys.maxsize

for i in range(n):
    for j in range(m):
        
        for height in range(1, n - i + 1):
            for width in range(1, m - j + 1):

                cnt = 0
                is_success = True

                for h in range(i, i + height):
                    for w in range(j, j + width):
                        if grid[h][w] <= 0:
                            is_success = False
                        cnt += 1
                
                if is_success:
                    ans = max(ans, cnt)

print(ans) if ans > 0 else print(-1)
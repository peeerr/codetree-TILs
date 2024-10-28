import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = -sys.maxsize

for i in range(n):
    for j in range(m):
        
        for height_1 in range(1, n - i + 1):
            for width_1 in range(1, m - j + 1):
                total = 0
                visited = [[False for _ in range(m)] for _ in range(n)]
                
                for h in range(i, i + height_1):
                    for w in range(j, j + width_1):
                        total += grid[h][w]
                        visited[h][w] = True

                for k in range(n):
                    for l in range(m):
                        if visited[k][l]:
                            continue
                        
                        for height_2 in range(1, n - k + 1):
                            for width_2 in range(1, m - l + 1):
                                is_success = True
                                sum_rectangle_2 = 0

                                for h in range(k, k + height_2):
                                    for w in range(l, l + width_2):
                                        if visited[h][w]:
                                            is_success = False
                                        sum_rectangle_2 += grid[h][w]
                                
                                if is_success:
                                    total += sum_rectangle_2
                                    ans = max(ans, total)
                                    total -= sum_rectangle_2

print(ans)
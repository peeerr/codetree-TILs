n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

ans = 0

for i in range(n):
    for j in range(n):

        if not in_range(i + 2, j + 2):
            continue
        
        cnt = 0
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                if grid[k][l] == 1:
                    cnt += 1

        ans = max(ans, cnt)

print(ans)
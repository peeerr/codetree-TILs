def is_happy(lst):
    cnt, max_cnt = 1, 1

    for i in range(n - 1):
        if lst[i] == lst[i + 1]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt >= m


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    ans += is_happy(grid[i][:])

for j in range(n):
    lst = []
    for i in range(n):
        lst.append(grid[i][j])
    ans += is_happy(lst)

print(ans)
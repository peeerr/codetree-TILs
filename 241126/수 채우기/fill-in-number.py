MAX_NUM = 100000

n = int(input())
ans = MAX_NUM

for i in range(MAX_NUM):
    remainder = n - 5 * i
    if remainder >= 0 and remainder % 2 == 0:
        ans = min(ans, remainder // 2 + i)

print(-1 if ans == MAX_NUM else ans)

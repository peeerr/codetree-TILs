n = int(input())
arr = list(map(int, input().split()))

ans = 0

for k in range(1, 101):
    cnt = 0
    for i in range(n):
        for j in range(i + 2, n):
            if k - i == j - k:
                cnt += 1
    ans = max(ans, cnt)

print(ans)
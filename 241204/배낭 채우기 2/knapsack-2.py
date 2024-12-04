n, m = map(int, (input().split()))
infos = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(m + 1)]

for i in range(m + 1):
    for w, v in infos:
        if i >= w:
            dp[i] = max(dp[i], dp[i - w] + v)
        

print(dp[m])

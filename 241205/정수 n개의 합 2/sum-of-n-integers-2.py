import sys


n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + arr[i - 1]

ans = -sys.maxsize
for i in range(k, n + 1):
    ans = max(ans, dp[i] - dp[i - k])

print(ans)

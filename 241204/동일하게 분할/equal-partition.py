n = int(input())
arr = list(map(int, input().split()))
m = sum(arr) // 2

dp = [0 for _ in range(m + 1)]

for x in arr:
    for i in range(m, -1, -1):
        if i >= x:
            dp[i] = max(dp[i], dp[i - x] + x)

print('Yes' if dp[m] == m else 'No')

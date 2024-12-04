n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    max_num = -1
    for j in range(i):
        if arr[j] < arr[i]:
            max_num = max(max_num, dp[j] + 1)
    if max_num == -1:
        dp[i] = 1
    else:
        dp[i] = max_num

print(max(dp))

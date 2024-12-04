n = int(input())
arr = list(map(int, input().split()))
m = sum(arr) // 2

dp = [False] * (m + 1) 
dp[0] = True 

for x in arr:
    for i in range(m, x - 1, -1):
        dp[i] |= dp[i - x]

if dp[m] and sum(arr) != m:
    print("Yes")
else:
    print("No")

import sys


n = int(input())
arr = list(map(int, input().split()))

if sum(arr) % 2 != 0:
    print('No')
    sys.exit(0)

m = sum(arr) // 2
dp = [False] * (m + 1) 
dp[0] = True 

for x in arr:
    for i in range(m, x - 1, -1):
        dp[i] |= dp[i - x]

print('Yes' if dp[m] else 'No')

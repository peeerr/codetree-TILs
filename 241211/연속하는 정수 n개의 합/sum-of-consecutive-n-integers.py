n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
sum_val, j = 0, 0

for i in range(n):
    while j < n and sum_val + arr[j] <= k:
        sum_val += arr[j]
        j += 1

    if sum_val == k:
        ans += 1
    
    sum_val -= arr[i]

print(ans)

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = n + 1

sum_val = 0
j = 0
for i in range(1, n + 1):
    while j + 1 <= n:
        if sum_val >= k:
            break
        sum_val += arr[j + 1]
        j += 1
    
    if sum_val >= k:
        ans = min(ans, j - i + 1)
    sum_val -= arr[i]
    
print(ans if ans != n + 1 else -1)

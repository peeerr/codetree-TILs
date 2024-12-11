INT_MAX = 100000


n = int(input())
arr = [0] + list(map(int, input().split()))
counting = [0 for _ in range(INT_MAX + 1)]

ans, j = 0, 0

for i in range(1, n + 1):
    while j + 1 <= n and not counting[arr[j + 1]]:
        counting[arr[j + 1]] = 1
        j += 1

    ans = max(ans, j - i + 1)
    counting[arr[i]] = 0

print(ans) 

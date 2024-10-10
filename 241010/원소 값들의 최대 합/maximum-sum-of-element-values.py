n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for i in range(n):
    s = 0
    idx = i
    for _ in range(m):
        s += arr[idx]
        idx = arr[idx] - 1

    ans = max(ans, s)

print(ans)
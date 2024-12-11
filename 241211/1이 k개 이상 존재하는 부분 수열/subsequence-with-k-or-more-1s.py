n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = n
cnt, j = 0, 0

for i in range(1, n + 1):
    while j + 1 <= n and cnt != k:
        if arr[j + 1] == 1:
            cnt += 1
        j += 1

    if cnt == k:
        ans = min(ans, j - i + 1)

    if arr[i] == 1:
        cnt -= 1

print(ans if ans != n else -1)

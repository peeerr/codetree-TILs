def possible(k):
    a = 0
    for x in arr:
        a += x // k
    return a >= m


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

ans = 0
left, right = 1, max(arr)

while left <= right:
    mid = (left + right) // 2
    if possible(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)

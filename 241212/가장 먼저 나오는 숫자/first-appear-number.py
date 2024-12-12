def lower_bound(target):
    left, right = 0, n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
            
    return min_idx


n, m = map(int, input().split())
arr = list(map(int, input().split()))

for x in map(int, input().split()):
    idx = lower_bound(x) + 1
    if arr[idx] == x:
        print(idx)
    else:
        print(-1)

def upper_bound(target):
    left, right = 0, n - 1
    min_idx = n
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_idx


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
arr = sorted(map(int, input().split()))
targets = [tuple(map(int, input().split())) for _ in range(m)]

for start, end in targets:
    print(upper_bound(end) - lower_bound(start))
    
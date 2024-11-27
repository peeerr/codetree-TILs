def lower(target):
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


def upper(target):
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


n, m = map(int, input().split())
arr = list(map(int, input().split()))
params = list(map(int, input().split()))

for param in params:
    lower_idx, upper_idx = lower(param), upper(param)

    if upper_idx - lower_idx:
        print(lower_idx + 1)
    else:
        print(-1)

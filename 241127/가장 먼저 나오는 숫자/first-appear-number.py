def binary_search(target):
    left, right = 0, n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return idx


n, m = map(int, input().split())
arr = list(map(int, input().split()))
params = list(map(int, input().split()))

for param in params:
    idx = binary_search(param)
    if arr[idx] == param:
        print(idx + 1)
    else:
        print(-1)

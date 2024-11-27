def binary_search(start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid + 1
    elif arr[mid] > target:
        return binary_search(start, mid - 1, target)
    else:
        return binary_search(mid + 1, end, target)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
targets = [int(input()) for _ in range(m)]

for target in targets:
    print(binary_search(0, n - 1, target))

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merge(low, mid, high)


def merge(low, mid, high):
    merged = []
    l, r = low, mid + 1

    while l <= mid and r <= high:
        if arr[l] <= arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1

    while l <= mid:
        merged.append(arr[l])
        l += 1

    while r <= high:
        merged.append(arr[r])
        r += 1

    for i in range(low, high + 1):
        arr[i] = merged[i - low]


n = int(input())
arr = list(map(int, input().split()))

merge_sort(0, n - 1)

print(*arr)

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merge(low, mid, high)


def merge(low, mid, high):
    l, r = low, mid + 1
    k = low

    while l <= mid and r <= high:
        if arr[l] <= arr[r]:
            merged_arr[k] = arr[l]
            l += 1
            k += 1
        else:
            merged_arr[k] = arr[r]
            r += 1
            k += 1

    while l <= mid:
        merged_arr[k] = arr[l]
        l += 1
        k += 1

    while r <= high:
        merged_arr[k] = arr[r]
        r += 1
        k += 1

    for i in range(low, high + 1):
        arr[i] = merged_arr[i]


n = int(input())
arr = list(map(int, input().split()))
merged_arr = [0] * n

merge_sort(0, n - 1)

print(*arr)

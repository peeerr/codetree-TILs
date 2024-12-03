n = int(input())
arr = list(map(int, input().split()))


def quick_sort(low, high):
    if low < high:
        pivot = partition(low, high)
        quick_sort(low, pivot - 1)
        quick_sort(pivot + 1, high)


def partition(low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


quick_sort(0, n - 1)

print(*arr)

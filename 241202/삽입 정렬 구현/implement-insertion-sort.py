n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    idx, value = i - 1, arr[i]

    while idx >= 0 and arr[idx] > value:
        arr[idx + 1] = arr[idx]
        idx -= 1
    
    arr[idx + 1] = value

print(*arr)

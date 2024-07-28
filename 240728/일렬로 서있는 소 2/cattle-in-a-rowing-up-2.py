n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] <= arr[j] <= arr[k]:
                ans += 1

print(ans)
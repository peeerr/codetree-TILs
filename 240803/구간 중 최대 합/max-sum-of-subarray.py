n, k = map(int, input().split())
arr = list(map(int, input().split()))

res = 0

for i in range(n - k + 1):
    tmp = arr[i]
    for j in range(i + 1, i + k):
        tmp += arr[j]
    res = max(res, tmp)

print(res)
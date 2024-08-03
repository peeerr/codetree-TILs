n, k = map(int, input().split())
arr = [0 for _ in range(601)]

for _ in range(n):
    info = tuple(map(int, input().split()))
    arr[info[1]] += info[0]

res = 0

for i in range(1 + k, 601 - k):
    tmp = 0
    for j in range(i - k, i + k + 1):
        tmp += arr[j]
    res = max(res, tmp)

print(res)
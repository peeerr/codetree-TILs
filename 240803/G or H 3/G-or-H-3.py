n, k = map(int, input().split())
arr = [0 for _ in range(10001)]

for _ in range(n):
    info = input().split()
    arr[int(info[0])] = info[1]

res = 0

for i in range(1, 10000 - k):
    tmp = 0
    for j in range(i, i + k + 1):
        if arr[j] == 'G':
            tmp += 1
        elif arr[j] == 'H':
            tmp += 2
    res = max(res, tmp)

print(res)
n, b = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

res = 0

for i in range(n):
    s, cnt = 0, 0
    for j in range(n):
        
        if j == i:
            s += arr[j] / 2
        else:
            s += arr[j]

        if s <= b:
            cnt += 1

    res = max(res, cnt)

print(res)
import sys

n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

res = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        cnt, cost = 0, 0
        for k in range(i, j + 1):
            cost += abs(h - arr[k])
            cnt += 1
            if cnt == t:
                break
        if cnt == t:
            res = min(res, cost)

print(res)
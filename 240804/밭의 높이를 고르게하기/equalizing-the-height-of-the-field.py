import sys

n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

res = sys.maxsize

for i in range(n - t):
    cost = 0
    for j in range(i, i + t):
        cost += abs(h - arr[j])
    res = min(res, cost)

print(res)
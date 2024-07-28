import sys

n = int(input())
arr = list(map(int, input().split()))

min_dist = sys.maxsize

for i in range(n):
    res = 0
    for j, x in enumerate(arr):
        res = res + (abs(i - j) * x)
    min_dist = min(min_dist, res)

print(min_dist)
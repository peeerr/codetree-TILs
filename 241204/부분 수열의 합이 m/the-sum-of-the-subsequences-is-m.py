import sys

MAX_INT = sys.maxsize


n, m = map(int, input().split())
arr = list(map(int, input().split()))

d = [MAX_INT for _ in range(m + 1)]
d[0] = 0

for x in arr:
    for i in range(m, -1, -1):
        if i >= x:
            d[i] = min(d[i], d[i - x] + 1)

print(-1 if d[m] == MAX_INT else d[m])

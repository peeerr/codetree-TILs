from collections import defaultdict
import sys

n = int(input())

d = defaultdict(lambda: sys.maxsize)

for _ in range(n):
    x, y = map(int, input().split())
    d[x] = min(d[x], y)

print(sum(d.values()))

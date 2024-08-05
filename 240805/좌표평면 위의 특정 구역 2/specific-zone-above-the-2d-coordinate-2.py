import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = sys.maxsize

for i in range(n):
    max_h, min_h = -sys.maxsize, sys.maxsize
    max_u, min_u = -sys.maxsize, sys.maxsize
    for j in range(n):
        if i == j:
            continue
        
        max_h, min_h = max(max_h, arr[j][1]), min(min_h, arr[j][1])
        max_u, min_u = max(max_u, arr[j][0]), min(min_u, arr[j][0])

    res = min(res, (max_h - min_h) * (max_u - min_h))
        
print(res)
import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = sys.maxsize

for i in range(n):
    max_x, min_x = -sys.maxsize, sys.maxsize
    max_y, min_y = -sys.maxsize, sys.maxsize
    for j in range(n):
        if i == j:
            continue
        
        max_x, min_x = max(max_x, arr[j][1]), min(min_x, arr[j][1])
        max_y, min_y = max(max_y, arr[j][0]), min(min_y, arr[j][0])

    res = min(res, (max_x - min_x) * (max_y - min_y))
        
print(res)
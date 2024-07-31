import sys

n = int(input())
arr = [int(input()) for _ in range(n)]

res = sys.maxsize

for i in range(n):
    tmp, cnt = 0, 0
    for j in range(i, n + i):
        tmp += arr[j % n] * cnt
        cnt += 1
    res = min(res, tmp)

print(res)
import sys

n = int(input())
arr = list(map(int, input().split()))

res = -sys.maxsize

for i in range(len(arr)):
    for j in range(i + 2, len(arr)):
        res = max(res, arr[i] + arr[j])

print(res)
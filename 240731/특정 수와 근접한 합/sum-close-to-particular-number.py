import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

res = sys.maxsize
sum_num = sum(arr)

for i in range(n):
    for j in range(i + 1, n):
        res = min(res, abs(s - (sum_num - arr[i] - arr[j])))

print(res)
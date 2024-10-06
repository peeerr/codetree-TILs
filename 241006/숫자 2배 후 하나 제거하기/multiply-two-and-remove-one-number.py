import sys

n = int(input())
arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(n):
    for j in range(n):
        s = 0

        tmp = arr[:]
        tmp[i] *= 2
        tmp.pop(j)

        for k in range(len(tmp) - 1):
            s += abs(tmp[k] - tmp[k + 1])

        ans = min(ans, s)

print(ans)
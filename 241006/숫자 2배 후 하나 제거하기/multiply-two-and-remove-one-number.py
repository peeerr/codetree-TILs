import sys

n = int(input())
arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(n):
    for j in range(n):
        s = 0

        for k in range(n - 1):
            if k == j:
                continue

            if k == i:
                s += abs((arr[k] * 2) - arr[k + 1])
            elif k + 1 == i:
                s += abs(arr[k] - (arr[k + 1] * 2))
            else:
                s += abs(arr[k] - arr[k + 1])

        ans = min(ans, s)

print(ans)
k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

res = 0
lst = []

for i in range(n):
    for j in range(i + 1, n):
        a, b = arr[0][i], arr[0][j]
        cnt = 0
        for l in range(k):
            if b in arr[l][arr[l].index(a) + 1:]:
                cnt += 1
        if cnt == k:
            res += 1

print(res)
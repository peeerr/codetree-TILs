n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0

for i in range(n - m + 1):
    tmp = b[:]
    for j in range(i, i + m):
        if a[j] in tmp:
            tmp.remove(a[j])
            if len(tmp) == 0:
                res += 1

print(res)
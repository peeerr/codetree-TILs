n, k, T = input().split()
n = int(n); k = int(k)
s = [input() for _ in range(n)]

res = []
for x in s:
    cnt = 0
    if x.startswith(T):
        res.append(x)

print(sorted(res)[k - 1])
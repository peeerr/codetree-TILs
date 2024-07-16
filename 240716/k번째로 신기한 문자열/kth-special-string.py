n, k, T = input().split()
n = int(n); k = int(k)
s = [input() for _ in range(n)]

res = []
for x in s:
    cnt = 0
    for i in range(len(T)):
        if x[i % len(x)] == T[i]:
            cnt += 1
    if cnt == len(T):
        res.append(x)

print(sorted(res)[k - 1])
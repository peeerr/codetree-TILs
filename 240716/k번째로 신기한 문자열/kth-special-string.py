n, k, T = input().split()
n = int(n); k = int(k)
s = [input() for _ in range(n)]

def starts_with(a, b):
    for i in range(len(b)):
        if a[i % len(a)] != b[i]:
            return False
    return True

res = []
for x in s:
    cnt = 0
    if starts_with(x, T):
        res.append(x)

print(sorted(res)[k - 1])
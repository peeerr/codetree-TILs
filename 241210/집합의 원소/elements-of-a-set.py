def union(a, b):
    x, y = find(a), find(b)
    ufset[x] = y


def find(x):
    if ufset[x] == x:
        return x
    root = find(ufset[x])
    ufset[x] = root
    return root


n, m = map(int, input().split())
ufset = [i for i in range(n + 1)]

for _ in range(m):
    command, a, b = map(int, input().split())
    if not command:
        union(a, b)
    else:
        print(1 if find(a) == find(b) else 0)

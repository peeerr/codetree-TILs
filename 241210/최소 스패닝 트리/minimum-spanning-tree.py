def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n, m = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

uf = [i for i in range(n + 1)]
ans = 0

for edge in edges:
    v, u, w = edge
    if find(v) != find(u):
        union(v, u)
        ans += w

print(ans)

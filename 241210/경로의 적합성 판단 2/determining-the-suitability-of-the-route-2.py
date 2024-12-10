def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n, m, k = map(int, input().split())
uf = [i for i in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

path = tuple(map(int, input().split()))
is_possible = True

for i in range(k - 1):
    if find(path[i]) != find(path[i + 1]):
        is_possible = False
        break

print(1 if is_possible else 0)

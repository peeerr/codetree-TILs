INT_MAX = 100000


def union(x, y):
    X, Y = find(x), find(y)
    if X != Y:
        if size[X] > size[Y]:
            X, Y = Y, X
        uf[X] = Y
        size[Y] += size[X]
    return size[Y]


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n = int(input())
uf = [i for i in range(INT_MAX + 1)]
size = [1 for _ in range(INT_MAX + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    print(union(a, b))

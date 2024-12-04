n, m = map(int, input().split())
infos = [0] + [tuple(map(int, input().split())) for _ in range(n)]

d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = infos[i]
    for j in range(1, m + 1):
        if j >= w:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - w] + v)
        else:
            d[i][j] = d[i - 1][j]

print(d[n][m])

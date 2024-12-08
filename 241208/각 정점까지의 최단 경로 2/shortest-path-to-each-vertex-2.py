import sys

MAX_INT = sys.maxsize


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [[MAX_INT for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    dist[u][v] = min(dist[u][v], w)

for i in range(1, n + 1):
    dist[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == MAX_INT:
            print(-1, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

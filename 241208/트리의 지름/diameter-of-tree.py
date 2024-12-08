import sys

sys.setrecursionlimit(10000)


def dfs(start, total_dist):
    for v, w in tree[start]:
        if not visited[v]:
            visited[v] = True
            dist[v] = total_dist + w
            dfs(v, total_dist + w)


n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

dist = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

visited[1] = True
dfs(1, 0)

max_v, max_dist = 0, 0
for i in range(1, n + 1):
    if dist[i] > max_dist:
        max_dist = dist[i]
        max_v = i

dist = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

visited[max_v] = True
dfs(max_v, 0)

print(max(dist))

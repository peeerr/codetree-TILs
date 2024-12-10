import sys, heapq

INT_MAX = sys.maxsize


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [False for _ in range(n + 1)]
dist = [INT_MAX for _ in range(n + 1)]

dist[1] = 0
pq = [(0, 1)]

ans = sum([k * i for i in range(n - 1)])

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if visited[min_idx]:
        continue

    visited[min_idx] = True
    ans += min_dist

    for v, w in graph[min_idx]:
        if w < dist[v]:
            dist[v] = w
            heapq.heappush(pq, (w, v))

print(ans)

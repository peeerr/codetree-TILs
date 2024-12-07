import sys, heapq

MAX_INT = sys.maxsize


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

a, b = map(int, input().split())
dist = [MAX_INT for _ in range(n + 1)]
dist[a] = 0
pq = [(0, a)]

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if dist[min_idx] != min_dist:
        continue

    for u, w in graph[min_idx]:
        new_dist = min_dist + w

        if new_dist < dist[u]:
            dist[u] = new_dist
            heapq.heappush(pq, (new_dist, u))

print(dist[b])

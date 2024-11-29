import heapq, sys

MAX_INT = sys.maxsize


n, m = map(int, input().split())

graph = [dict() for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[v][u] = w

dist = [MAX_INT for _ in range(n + 1)]
dist[n] = 0

pq = []
heapq.heappush(pq, (0, n))

while pq:
    min_dist, u = heapq.heappop(pq)

    if min_dist != dist[u]:
        continue

    for v, weight in graph[u].items():
        if dist[v] > weight + min_dist:
            dist[v] = weight + min_dist
            heapq.heappush(pq, (weight + min_dist, v))

print(max([x for x in dist if x != MAX_INT]))

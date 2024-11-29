import heapq


n, m = map(int, input().split())

graph = [dict() for _ in range(n + 1)]

for _ in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1][v2] = w


dist = [float('inf') for _ in range(n + 1)]
pq = []

dist[1] = 0
heapq.heappush(pq, (0, 1))


while pq:
    dist_u, u = heapq.heappop(pq)

    for v in graph[u].keys():
        new_dist = graph[u][v] + dist_u
        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))


for i in range(2, n + 1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])

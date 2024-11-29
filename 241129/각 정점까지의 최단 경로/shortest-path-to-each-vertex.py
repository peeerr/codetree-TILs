import heapq


n, m = map(int, input().split())
k = int(input())

graph = [dict() for _ in range(n + 1)]

for _ in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1][v2] = w
    graph[v2][v1] = w


dist = [float('inf') for _ in range(n + 1)]
pq = []

dist[k] = 0
heapq.heappush(pq, (0, k))


while pq:
    dist_u, u = heapq.heappop(pq)

    if dist_u != dist[u]:
        continue
 
    for v, weight in graph[u].items():
        new_dist = weight + dist_u
        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))


for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])

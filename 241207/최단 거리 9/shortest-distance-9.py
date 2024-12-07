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
path = [0 for _ in range(n + 1)]

pq = []
heapq.heappush(pq, (0, a))
dist[a] = 0

while pq:
    min_dist, v = heapq.heappop(pq)

    if dist[v] != min_dist:
        continue

    for u, w in graph[v]:
        if min_dist + w < dist[u]:
            dist[u] = min_dist + w
            heapq.heappush(pq, (min_dist + w, u))
            path[u] = v

ans = []
curr_v = b

while curr_v != 0:
    ans.append(curr_v)
    curr_v = path[curr_v]

print(dist[b])
print(*ans[::-1])

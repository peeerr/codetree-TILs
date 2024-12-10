import sys, heapq

INT_MAX = sys.maxsize


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[v].append((u, w))
    graph[u].append((v, w))

dist = [INT_MAX for _ in range(n + 1)]

# 아무 정점에서 시작
dist[1] = 0
pq = [(0, 1)]

ans = 0

while pq:
    min_dist, min_v = heapq.heappop(pq)

    if dist[min_v] != min_dist:
        continue
    
    ans += min_dist

    for u, w in graph[min_v]:
        if w < dist[u]:
            dist[u] = w
            heapq.heappush(pq, (w, u))

print(ans)

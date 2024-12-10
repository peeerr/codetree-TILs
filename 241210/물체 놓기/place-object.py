import sys, heapq

INT_MAx = sys.maxsize


n = int(input())

cost = [int(input()) for _ in range(n)]
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j, w in enumerate(list(map(int, input().split())), start=1):
        if i != j:
            graph[i].append((j, w))

visited = [False for _ in range(n + 1)]
dist = [INT_MAx for _ in range(n + 1)]

dist[1] = 0
pq = [(0, 1)]

ans = 0

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

print(ans + min(cost))

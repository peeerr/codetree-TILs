import sys, heapq

INF = sys.maxsize

# 입력 받기
n, m = map(int, input().split())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력 (양방향)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

# 시작점, 도착점 입력
a, b = map(int, input().split())

# 다익스트라 알고리즘
dist = [INF] * (n + 1)
dist[b] = 0
pq = [(0, b)]  # (거리, 노드)

while pq:
    d, curr = heapq.heappop(pq)
    
    if dist[curr] < d:
        continue
        
    for next_node, weight in graph[curr]:
        next_dist = d + weight
        
        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))

# 최단 거리 출력
print(dist[a])

# 경로 역추적
curr = a
print(curr, end=" ")

while curr != b:
    for next_node, weight in sorted(graph[curr]):  # 번호가 작은 순서대로 확인
        if dist[curr] == dist[next_node] + weight:
            curr = next_node
            print(curr, end=" ")
            break

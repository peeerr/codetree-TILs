import sys, heapq

n = int(input())

# 각 정점에 직접 물체를 놓는 비용
cost = [int(input()) for _ in range(n)]

# 그래프 초기화 (0-based indexing으로 수정)
graph = [[] for _ in range(n)]

# 간선 정보 입력 받기
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if i != j:  # 자기 자신으로의 간선은 제외
            graph[i].append((j, row[j]))

def find_min_cost(start):
    visited = [False for _ in range(n)]
    dist = [float('inf') for _ in range(n)]
    
    # 시작 정점 초기화
    dist[start] = cost[start]  # 시작 정점은 직접 물체를 놓는 비용으로 초기화
    pq = [(cost[start], start)]
    
    total_cost = 0
    while pq:
        min_dist, curr = heapq.heappop(pq)
        
        if visited[curr]:
            continue
            
        visited[curr] = True
        total_cost += min_dist
        
        # 현재 정점에서 이동 가능한 모든 정점에 대해
        for next_vertex, weight in graph[curr]:
            if not visited[next_vertex]:
                # 간선을 통해 연결하는 비용과 직접 물체를 놓는 비용 중 최소값 선택
                next_cost = min(weight, cost[next_vertex])
                if next_cost < dist[next_vertex]:
                    dist[next_vertex] = next_cost
                    heapq.heappush(pq, (next_cost, next_vertex))
    
    return total_cost

# 모든 정점을 시작점으로 시도해보고 최소 비용 찾기
min_total_cost = float('inf')
for start in range(n):
    min_total_cost = min(min_total_cost, find_min_cost(start))

print(min_total_cost)

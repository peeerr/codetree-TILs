def dfs(start):
    for v in graph[start]:
        if not visited[v]:
            visited[v] = True
            parent[v] = start
            dfs(v)


n = int(input())
graph = [[] for _ in range(n + 1)]
parent = {}

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False for _ in range(n + 1)]
visited[1] = True
dfs(1)

for i in range(2, n + 1):
    print(parent[i])

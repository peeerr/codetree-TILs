def dfs(v):
    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            ans.append(u)
            dfs(u)


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

path = tuple(map(int, input().split()))

visited = [False for _ in range(n + 1)]
visited[1] = True
ans = [1]

dfs(1)

is_possible = True
for x in path:
    if x not in ans:
        is_possible = False
        break

print(1 if is_possible else 0)

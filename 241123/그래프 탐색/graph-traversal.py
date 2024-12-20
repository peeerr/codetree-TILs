def dfs(curr_v):
    global ans

    for v in graph[curr_v]:
        if not visited[v]:
            ans += 1
            visited[v] = True
            dfs(v)


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
ans = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited[1] = True
dfs(1)

print(ans)

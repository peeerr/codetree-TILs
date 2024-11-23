from collections import defaultdict


def dfs(curr_v):
    global ans

    for v in graph[curr_v]:
        if not visited[v]:
            ans += 1
            visited[v] = True
            dfs(v)


n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(len(graph) + 1)]
ans = 0

visited[1] = True
dfs(1)

print(ans)

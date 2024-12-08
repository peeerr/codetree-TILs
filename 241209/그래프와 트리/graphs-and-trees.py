def dfs(start):
    global edge_cnt, v_cnt
    for v in graph[start]:
        edge_cnt += 1
        if not visited[v]:
            visited[v] = True
            v_cnt += 1
            dfs(v)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n + 1)]
ans = 0

for i in range(1, n + 1):
    if visited[i]:
        continue

    edge_cnt, v_cnt = 0, 1
    visited[i] = True
    dfs(i)

    if v_cnt - 1 == edge_cnt // 2:
        ans += 1

print(ans)

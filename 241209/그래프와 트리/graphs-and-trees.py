def dfs(start):
    global edge_cnt
    for v in graph[start]:
        edge_cnt += 1
        if not visited[v]:
            visited[v] = True
            dfs(v)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, = map(int, input().split())
    graph[u].append(v)

visited = [False for _ in range(n + 1)]
ans = 0

for i in range(1, n + 1):
    if not visited[i]:
        edge_cnt, prev_v_cnt = 0, len(visited) - 1 - len([x for x in visited[1:] if x])
        visited[i] = True
        dfs(i)
        v_cnt = prev_v_cnt - len([x for x in visited[1:] if not x])
        if v_cnt - 1 == edge_cnt:
            ans += 1

print(ans)

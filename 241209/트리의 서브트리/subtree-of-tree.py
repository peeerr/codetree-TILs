def dfs(node):
    for v in tree[node]:
        if not visited[v]:
            visited[v] = True
            dfs(v)
            dp[node] += dp[v]


n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = {i:1 for i in range(1, n + 1)}
visited = [False for _ in range(n + 1)]

visited[r] = True
dfs(r)

for _ in range(q):
    u = int(input())
    print(dp[u])

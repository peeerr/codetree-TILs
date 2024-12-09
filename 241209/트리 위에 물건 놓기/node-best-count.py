import sys

INT_MAX = sys.maxsize


def dfs(node):
    for v in tree[node]:
        if not visited[v]:
            visited[v] = True
            parent[v] = node
            dfs(v)

    dp[node][0] = 0
    dp[node][1] = 1

    for v in tree[node]:
        if parent[v] != node:
            continue
        dp[node][0] += dp[v][1]
        dp[node][1] += min(dp[v][0], dp[v][1])


n = int(input())
tree = [[] for _ in range(n + 1)]
dp = [[INT_MAX for _ in range(2)] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False for _ in range(n + 1)]
visited[1] = True
dfs(1)

print(min(dp[1][0], dp[1][1]))

import sys

INT_MAX = sys.maxsize


def dfs(node):
    for v in tree[node]:
        if not visited[v]:
            visited[v] = True
            dfs(v)
            dp[node][0] += dp[v][1]
            dp[node][1] += min(dp[v])


n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

already = tuple(map(int, input().split()))

visited = [False for _ in range(n + 1)]
dp = [[0, 1] for _ in range(n + 1)]

for x in already:
    dp[x] = [INT_MAX, 0]

visited[1] = True
dfs(1)

print(min(dp[1]))

def dfs(node):
    for v in tree[node]:
        if not visited[v]:
            visited[v] = True
            dfs(v)

    for v in tree[node]:
        if nums[v] > 0:
            nums[node] += nums[v]


n = int(input())
tree = [[] for _ in range(n + 1)]
nums = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    t, a, p = map(int, input().split())

    if t:
        tree[p].append(i)
        nums[i] = a
    else:
        tree[p].append(i)
        nums[i] = -a

visited = [False for _ in range(n + 1)]
visited[1] = True
dfs(1)

print(nums[1])

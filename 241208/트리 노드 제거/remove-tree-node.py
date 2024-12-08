def remove(start):
    for v in tree[start]:
        if not visited[v]:
            visited[v] = True
            remove(v)


n = int(input())
parents = list(map(int, input().split()))
tree = [[] for _ in range(n)]

for child, parent in enumerate(parents):
    if parent == -1:
        continue
    tree[parent].append(child)

x = int(input())
visited = [False for _ in range(n)]
visited[x] = True

if x in tree[parents[x]]:
    tree[parents[x]].remove(x)

remove(x)
ans = 0

for i in range(n):
    if visited[i]:
        continue
    if not len(tree[i]):
        ans += 1

print(ans)

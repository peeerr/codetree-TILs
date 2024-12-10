def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n, m = map(int, input().split())
v_type = [''] + input().split()
edges = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

uf = [i for i in range(n + 1)]
ans, selected_edge_cnt = 0, 0

for v, u, w in edges:
    if find(v) != find(u) and v_type[v] != v_type[u]:
        ans += w
        selected_edge_cnt += 1
        union(v, u)

print(ans if selected_edge_cnt == n - 1 else -1)

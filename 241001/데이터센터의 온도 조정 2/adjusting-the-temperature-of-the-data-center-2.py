def seek(t, ta, tb):
    if t < ta:
        return c
    elif ta <= t <= tb:
        return g
    else:
        return h


n, c, g, h = map(int, input().split())
temperature = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for t in range(1001):
    s = 0
    for tp in temperature:
        s += seek(t, tp[0], tp[1])
    ans = max(ans, s)

print(ans)
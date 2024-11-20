def calc(infos):
    result = [i for i in range(n + 1)]

    for w, h in infos:
        result[w], result[w + 1] = result[w + 1], result[w]
    
    return result[1:]


def f(idx):
    global ans

    if idx == m:
        return

    for i in range(idx, m):
        selected.append(infos[i])

        res = calc(selected)
        if res == result:
            ans = min(ans, len(selected))

        f(i + 1)
        selected.pop()


n, m = map(int, input().split())
infos = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x : (x[1], x[0]))

selected = []
ans = m

result = calc(infos)
res = calc([])

if res == result:
    print(0)
else:
    f(0)
    print(ans)

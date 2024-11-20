def judge():
    length = len(selected)

    for i in range(length):
        for j in range(i + 1, length):
            x1, x2 = selected[i]
            x3, x4 = selected[j]

            if x3 <= max(x1, x2) <= x4:
                return False
            elif x3 <= min(x1, x2) <= x4:
                return False
    
    return True


def f(k):
    global ans

    if k == n:
        return

    for i in range(n):
        if infos[i] in selected:
            continue

        selected.append(infos[i])
        if judge():
            ans = max(ans, len(selected))
        f(k + 1)
        selected.pop()


n = int(input())
infos = [tuple(map(int, input().split())) for _ in range(n)]
selected = []
ans = 0

f(0)

print(ans)

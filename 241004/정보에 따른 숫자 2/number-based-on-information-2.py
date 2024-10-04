t, a, b = map(int, input().split())
arr = [list(map(lambda x : int(x) if x.isdigit() else x, input().split())) for _ in range(t)]

ans = 0

for k in range(a, b + 1):
    d1, d2 = 1000, 1000
    for c, x in arr:
        if c == 'S':
            d1 = min(d1, abs(k - x))
        elif c == 'N':
            d2 = min(d2, abs(k - x))

    if d1 <= d2:
        ans += 1

print(ans)
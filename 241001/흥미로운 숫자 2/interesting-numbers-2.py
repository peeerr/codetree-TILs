x, y = map(int, input().split())

ans = 0

for num in range(x, y + 1):
    tmp = [0 for _ in range(10)]

    for x in map(int, str(num)):
        tmp[x] += 1

    if tmp.count(1) == 1 and tmp.count(0) == 8:
        ans += 1

print(ans)
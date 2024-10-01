x, y = map(int, input().split())

ans = 0

for num in range(x, y + 1):
    tmp = [0 for _ in range(10)]

    for x in map(int, str(num)):
        tmp[x] += 1

    success = 0
    for x in tmp:
        if x >= 2:
            success += 1
        elif x == 1:
            success += 1

    if success == 2:
        ans += 1

print(ans)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n):
    is_ok = True
    for j in range(n):
        if i == j:
            continue

        x1, x2 = arr[i][0], arr[i][1]
        x3, x4 = arr[j][0], arr[j][1]

        if (x1 < x3 and x2 > x4) or (x1 > x3 and x2 < x4):
            is_ok = False
            break

    if is_ok:
        res += 1

print(res)
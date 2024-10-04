x, y = map(int, input().split())

ans = 0

for n in range(x, y + 1):
    num = str(n)

    if num == num[::-1]:
        ans += 1

print(ans)
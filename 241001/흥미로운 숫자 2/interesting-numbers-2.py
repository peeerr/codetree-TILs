x, y = map(int, input().split())

ans = 0

for num in range(x, y + 1):
    if len(set(str(num))) == 2:
        ans += 1

print(ans)
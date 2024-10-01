x, y = map(int, input().split())

ans = 0

for num in range(x, y + 1):
    ans = max(ans, sum(tuple(map(int, str(num)))))

print(ans)
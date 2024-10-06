a, b, c = map(int, input().split())

ans = 0

for i in range(1000):
    for j in range(1000):
        
        s = (a * i) + (b * j)

        if s <= c:
            ans = max(ans, s)

print(ans)
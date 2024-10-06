a, b, c = map(int, input().split())

ans = 0

for i in range(c // a + 1):
    s = a * i
    s = s + b * ((c - s) // b)
    ans = max(ans, s)

print(ans)
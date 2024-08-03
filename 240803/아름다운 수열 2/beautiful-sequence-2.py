n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0

for i in range(n - m + 1):
    if sorted(a[i:i + m]) == sorted(b):
        res += 1

print(res)
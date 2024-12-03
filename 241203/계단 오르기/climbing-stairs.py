n = int(input())
d = [0 for _ in range(1001)]

d[2] = 1
d[3] = 1

for i in range(4, n + 1):
    d[i] = d[i - 2] + d[i - 3]

print(d[n] % 10007)

n = int(input())
d = [0] * (n + 1)

d[0] = 1
d[1] = 1

for i in range(2, n + 1):
    s = 0
    for j in range(1, i + 1):
        s += d[j - 1] * d[i - j]
    d[i] = s

print(d[n])

m1, d1, m2, d2 = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

res = 1
for m in range(m1, m2):
    res += days[m]

print(res - d1 + d2)
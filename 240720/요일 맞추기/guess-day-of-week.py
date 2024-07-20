m1, d1, m2, d2 = map(int, input().split())

dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

res = 0
for i in range(min(m1, m2), max(m1, m2)):
    res += dates[i]
res += d2 - d1

print(days[res % 7])
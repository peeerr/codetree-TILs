m1, d1, m2, d2 = map(int, input().split())

dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

res = 0
if m1 <= m2:
    for i in range(m1, m2):
        res += dates[i]
    res += d2 - d1
else:
    for i in range(m2, m1):
        res -= dates[i]
    res += d2 - d1
    
print(days[res % 7])
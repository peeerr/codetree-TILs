def cal_days(month, day):
    res = 0
    for i in range(1, month):
        res += dates[i]
    return res + day 


m1, d1, m2, d2 = map(int, input().split())

dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

diff = cal_days(m2, d2) - cal_days(m1, d1)

print(days[diff % 7])
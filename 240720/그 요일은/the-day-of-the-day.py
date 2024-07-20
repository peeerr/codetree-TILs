def cal_date(month, day):
    dates = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    res = 0
    for i in range(1, month):
        res += dates[i]
    return res + day


m1, d1, m2, d2 = map(int, input().split())
a = input()

diff = cal_date(m2, d2) - cal_date(m1, d1)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

cnt = 0
for k in range(diff + 1):
    if days[k % 7] == a:
        cnt += 1

print(cnt)
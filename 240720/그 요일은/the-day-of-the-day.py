m1, d1, m2, d2 = map(int, input().split())
a = input()

dates = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

diff = (sum(dates[1: m2 + 1]) + d2) - (sum(dates[1: m1 + 1]) + d1) + 1

idx = days.index(a)

print(((diff - idx) // 7) + 1)

# cnt = 0
# for k in range(diff + 1):
#     if days[k % 7] == a:
#         cnt += 1

# print(cnt)
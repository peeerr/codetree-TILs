class Info():
    def __init__(self, date, week, weather):
        self.date = date
        self.week = week
        self.weather = weather

n = int(input())
infos = sorted([Info(*input().split()) for _ in range(n)], key=lambda x : x.weather)

for info in infos:
    if info.weather == 'Rain':
        print(info.date, info.week, info.weather)
        break
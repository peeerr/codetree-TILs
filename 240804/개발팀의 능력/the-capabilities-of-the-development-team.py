import sys

arr = list(map(int, input().split()))
n = len(arr)

res = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        for k in range(n):
            if i == k or j == k:
                continue
            
            team1 = arr[i] + arr[j]
            team2 = arr[k]
            team3 = sum(arr) - (arr[i] + arr[j] + arr[k])

            if team1 == team2 or team1 == team3 or team2 == team3:
                continue

            max_team = max(team1, team2, team3)
            min_team = min(team1, team2, team3)
            sub = max_team - min_team

            res = min(res, sub)

if res == sys.maxsize:
    print(-1)
else:
    print(res)
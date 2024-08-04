import sys

arr = list(map(int, input().split()))

res = sys.maxsize

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            team_sum = arr[i] + arr[j] + arr[k]
            res = min(res, abs(team_sum - (sum(arr) - team_sum)))

print(res)
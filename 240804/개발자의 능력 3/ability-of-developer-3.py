import sys

arr = list(map(int, input().split()))

res = sys.maxsize

for i in range(6):
    for j in range(6):
        for k in range(6):
            if i == j or i == k or j == k:
                continue
            team_sum = arr[i] + arr[j] + arr[k]
            res = min(res, abs(team_sum - (sum(arr) - team_sum)))

print(res)
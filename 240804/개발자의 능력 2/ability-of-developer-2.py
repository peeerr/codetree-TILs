import sys

arr = list(map(int, input().split()))
n = len(arr)

res = sys.maxsize

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i == j or i == k or i == l or j == k or j == l or k == l:
                    continue

                rest_team = sum(arr) - (arr[i] + arr[j] + arr[k] + arr[l])
                max_team = max(arr[i] + arr[j], arr[k] + arr[l], rest_team)
                min_team = min(arr[i] + arr[j], arr[k] + arr[l], rest_team)
                res = min(res, max_team - min_team)
                

print(res)
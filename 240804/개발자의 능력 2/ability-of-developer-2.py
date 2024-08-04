import sys

arr = list(map(int, input().split()))
n = len(arr)

res = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        for k in range(n):
            for l in range(k + 1, n):
                if k == i or i == l or j == k or j == l:
                    continue

                rest_team = sum(arr) - (arr[i] + arr[j] + arr[k] + arr[l])
                max_team = max(arr[i] + arr[j], arr[k] + arr[l], rest_team)
                min_team = min(arr[i] + arr[j], arr[k] + arr[l], rest_team)
                res = min(res, max_team - min_team)
                

print(res)
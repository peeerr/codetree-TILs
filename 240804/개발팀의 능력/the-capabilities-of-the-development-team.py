import sys

arr = list(map(int, input().split()))
n = len(arr)

res = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        for k in range(n):
            if i == k:
                continue
            
            rest_team = sum(arr) - (arr[i] + arr[j] + arr[k])
            max_team = max(arr[i] + arr[j], arr[k], rest_team)
            min_team = min(arr[i] + arr[j], arr[k], rest_team)
            sub = max_team - min_team

            if sub != 0:
                res = min(res, sub)

if res == sys.maxsize:
    print(-1)
else:
    print(res)
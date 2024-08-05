n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or i == k or j == k:
                continue
            
            width = max(arr[i][0], arr[j][0], arr[k][0]) - min(arr[i][0], arr[j][0], arr[k][0])
            height = max(arr[i][1], arr[j][1], arr[k][1]) - min(arr[i][1], arr[j][1], arr[k][1])
            area = width * height / 2

            res = max(res, area)

print(int(res * 2))
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or i == k or j == k:
                continue
            

            area = 0.5 * abs((arr[i][0] * arr[j][1] + arr[j][0] * arr[k][1] + arr[k][0] * arr[i][1]) - (arr[j][1] * arr[i][1] + arr[k][0] * arr[j][1] + arr[i][0] * arr[k][1]))

            if area == int(area):
                res = max(res, int(area))

print(res * 2)
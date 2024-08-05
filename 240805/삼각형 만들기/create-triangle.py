def check(i, j, k):
    if (arr[i][0] == arr[j][0] or arr[i][0] == arr[k][0] or arr[j][0] == arr[k][0]) and (arr[i][1] == arr[j][1] or arr[i][1] == arr[k][1] or arr[j][1] == arr[k][1]):
        return True
    return False


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or i == k or j == k or not check(i, j, k):
                continue

            area = abs((arr[i][0] * arr[j][1] + arr[j][0] * arr[k][1] + arr[k][0] * arr[i][1]) - (arr[j][0] * arr[i][1] + arr[k][0] * arr[j][1] + arr[i][0] * arr[k][1]))
            res = max(res, area)

print(res)
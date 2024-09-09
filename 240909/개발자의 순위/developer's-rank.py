k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

cnt = 0
lst = []

for i in range(n):
    for j in range(i + 1, n):
        lst.append((arr[0][i], arr[0][j]))

for x in lst:
    temp = 0
    for y in arr:
        if x[1] in y[y.index(x[0]) + 1 :]:
            temp += 1
    if temp == k:
        cnt += 1

print(cnt)
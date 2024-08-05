n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    line = [0 for _ in range(1001)]
    s = 0
    for j in range(n):
        if i == j:
            continue 

        for k in range(arr[j][0], arr[j][1]):
            line[k] += 1

    for x in line:
        if x != 0:
            s += 1
    res = max(res, s)

print(res)
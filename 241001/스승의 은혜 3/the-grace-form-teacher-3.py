import copy

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    tmp = copy.deepcopy(arr)
    tmp[i][0] /= 2

    sorted_arr = sorted(tmp, key=lambda x : x [0] + x[1])
    
    total, cnt = 0, 0
    for x in sorted_arr:
        total += x[0] + x[1]

        if total > b:
            total -= x[0] + x[1]
            break
        else:
            cnt += 1
    
    ans = max(ans, cnt)

print(ans)
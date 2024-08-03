n = int(input())
infos = [list(map(lambda x : int(x) if x.isdigit() else x, input().split())) for _ in range(n)]

length = max(infos, key=lambda x : x[0])[0]
arr = [0 for _ in range(length + 1)]

for info in infos:
    arr[info[0]] = info[1]

res = 0

for i in range(1, length + 1):
    if arr[i] in ['G', 'H']:
        for j in range(1, length + 1 - i):
            if arr[i + j] in ['G', 'H']:
                g, h = 0, 0
                for k in range(i, i + j + 1):
                    if arr[k] == 'G':
                        g += 1
                    elif arr[k] == 'H':
                        h += 1
                if (g != 0 and h != 0 and g == h) or (g == 0 and h == j - 1) or (h == 0 and g == j - 1):
                    res = max(res, j)
            
print(res)
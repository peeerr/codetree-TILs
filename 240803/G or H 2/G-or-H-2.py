n = int(input())
arr = [0 for _ in range(101)]

for _ in range(n):
    info = input().split()
    arr[int(info[0])] = info[1]

res = 0

for i in range(1, 101):
    if arr[i] in ['G', 'H']:
        for j in range(1, 101 - i):
            if arr[i + j] in ['G', 'H']:
                g, h = 0, 0
                for k in range(i, i + j + 1):
                    if arr[k] == 'G':
                        g += 1
                    elif arr[k] == 'H':
                        h += 1
                if (g == h != 0) or (g == 0 and h > 0) or (h == 0 and g > 0):
                    res = max(res, j)
            
print(res)
n = int(input())
arr = [0 for _ in range(101)]

for _ in range(n):
    info = input().split()
    arr[int(info[0])] = info[1]

res = 0

for i in range(1, 101):
    for j in range(i + 1, 101):
        if arr[i] == 0 or arr[j] == 0:
            continue
        
        g, h = 0, 0
        for k in range(i, j + 1):
            if arr[k] == 'G':
                g += 1
            elif arr[k] == 'H':
                h += 1

        if g == h or g == 0 or h == 0:
            res = max(res, j - i)
            
print(res)
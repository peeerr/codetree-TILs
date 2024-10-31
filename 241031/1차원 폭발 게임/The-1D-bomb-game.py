def cut():
    global n

    i = 0
    is_cut = False

    while i < n:
        start, cnt = i, 1
        i += 1
        
        while i + 1 < n and arr[i] == arr[i + 1]:
            cnt += 1
            i += 1
        
        if cnt >= m:
            for _ in range(cnt):
                arr.pop(start)
            n = len(arr)
            i = start
            is_cut = True

    return is_cut


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

if m == 1:
    print(0)
else:
    while cut():
        pass

    print(n)
    for x in arr:
        print(x)
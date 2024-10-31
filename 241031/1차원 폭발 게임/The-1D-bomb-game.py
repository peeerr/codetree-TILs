def cut(m):
    global n

    temp = []
    i = 0
    is_cut = False

    while i < n:
        if i + 1 < n and arr[i] == arr[i + 1]:
            idx, cnt = i + 1, 2

            while idx < n - 1:
                if arr[idx] != arr[idx + 1]:
                    break
                cnt += 1
                idx += 1
            
            if cnt >= m:
                is_cut = True
                i = idx + 1

        else:
            temp.append(arr[i])
            i += 1
    
    n = len(temp)
    for i in range(n):
        arr[i] = temp[i]

    return is_cut


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

while cut(m):
    pass

if n:
    print(n)
    for i in range(n):
        print(arr[i])
else:
    print(0)
def f(n):
    arr, pos = [0], 1
    for _ in range(n):
        v, t = map(int, input().split())
        for _ in range(t):
            arr.append(arr[pos - 1] + v)
            pos += 1
    return arr


n, m = map(int, input().split())

arr1, arr2 = f(n), f(m)

head, cnt = 0, 0
for x1, x2 in zip(arr1, arr2):
    if x1 > x2:
        if head == 2:
            cnt += 1
        head = 1
    elif x1 < x2:
        if head == 1:
            cnt += 1
        head = 2

print(cnt)
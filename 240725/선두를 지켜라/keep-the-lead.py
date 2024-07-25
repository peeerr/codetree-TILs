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

head = 'a' if arr1[1] > arr2[1] else 'b'
cnt = 0
for x1, x2 in zip(arr1, arr2):
    if x1 > x2 and head == 'b':
        cnt += 1
        head = 'a'
    elif x1 < x2 and head == 'a':
        cnt += 1
        head = 'b'

print(cnt)
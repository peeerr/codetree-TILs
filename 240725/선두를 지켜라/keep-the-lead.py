n, m = map(int, input().split())

arr1, pos = [0], 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        arr1.append(arr1[pos - 1] + v)
        pos += 1

arr2, pos = [0], 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        arr2.append(arr2[pos - 1] + v)
        pos += 1

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
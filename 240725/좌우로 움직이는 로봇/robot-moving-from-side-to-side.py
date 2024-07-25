n, m = map(int, input().split())

arr1, pos = [0], 1
for _ in range(n):
    t, d = input().split(); t = int(t)

    for _ in range(t):
        arr1.append(arr1[pos - 1] + (1 if d == 'R' else -1))
        pos += 1

arr2, pos = [0], 1
for _ in range(m):
    t, d = input().split(); t = int(t)

    for _ in range(t):
        arr2.append(arr2[pos - 1] + (1 if d == 'R' else -1))
        pos += 1

last, cnt, more = float('inf'), 0, 0
for i in range(1, max(len(arr1), len(arr2)) - 1):
    if i + 1 == len(arr1):
        last = arr1[i]
        more = 2
    elif i + 1 == len(arr2):
        last = arr2[i]
        more = 1

    if more == 0 and arr1[i] != arr2[i] and arr1[i + 1] == arr2[i + 1]:
        cnt += 1
    elif more == 1 and arr1[i + 1] == last:
        cnt += 1
    elif more == 2 and arr2[i + 1] == last:
        cnt += 1

print(cnt)
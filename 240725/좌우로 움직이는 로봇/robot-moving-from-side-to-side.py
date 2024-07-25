n, m = map(int, input().split())

arr1, pos1 = [0], 1
for _ in range(n):
    t, d = input().split(); t = int(t)
    for _ in range(t):
        arr1.append(arr1[pos1 - 1] + (1 if d == 'R' else -1))
        pos1 += 1

arr2, pos2 = [0], 1
for _ in range(m):
    t, d = input().split(); t = int(t)
    for _ in range(t):
        arr2.append(arr2[pos2 - 1] + (1 if d == 'R' else -1))
        pos2 += 1

while len(arr1) != len(arr2):
    if len(arr1) < len(arr2):
        arr1.append(arr1[-1])
    else:
        arr2.append(arr2[-1])

cnt = 0
for i in range(1, len(arr1) - 1):
    if arr1[i] != arr2[i] and arr1[i + 1] == arr2[i + 1]:
        cnt += 1

print(cnt)
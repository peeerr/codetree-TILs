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


# -1: arr1[i]가 더 큼 0: 같음 1: arr2[i]가 더 큼
cnt, prev_status, curr_status = 0, -2, -2

for i in range(1, min(len(arr1), len(arr2))):
    if arr1[i] > arr2[i]:
        curr_status = -1
    elif arr1[i] < arr2[i]:
        curr_status = 1
    else:
        curr_status = 0
    
    if prev_status != curr_status:
        cnt += 1
        prev_status = curr_status

print(cnt)
n = int(input())
arr = [int(input()) for _ in range(n)]

idx = 0
res = []

curr = 1
for i in range(len(arr) - 1):
    if arr[i] != arr[i + 1]:
        res.append((arr[i], abs(i - curr)))
        curr = i
    if i == len(arr) - 2 and arr[len(arr) - 1] == arr[len(arr) - 2]:
        res.append((arr[i], i + 1 - curr))
    if i == len(arr) - 2 and arr[len(arr) - 1] != arr[len(arr) - 2]:
        res.append((arr[i + 1], 1))

print(max(res, key=lambda x : x[1])[1])
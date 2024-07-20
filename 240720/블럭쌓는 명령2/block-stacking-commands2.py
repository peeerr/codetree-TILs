n, k = map(int, input().split())
inst = [list(map(int, input().split())) for _ in range(k)]

arr = [0 for _ in range(n)]

for x in inst:
    for i in range(x[0] - 1, x[1]):
        arr[i] += 1

print(max(arr))
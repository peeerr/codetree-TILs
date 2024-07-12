n, m = map(int, input().split())

arr = list(map(int, input().split()))
positions = [tuple(map(int, input().split())) for _ in range(m)]

for i, j in positions:
    res = 0
    for k in range(i - 1, j):
        res += arr[k]
    print(res)
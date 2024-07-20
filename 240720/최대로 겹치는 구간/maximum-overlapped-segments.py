n = int(input())
lines = [list(map(lambda x : int(x) + 100, input().split())) for _ in range(n)]

arr = [0 for _ in range(202)]

for x in lines:
    for i in range(x[0], x[1]):
        arr[i] += 1

print(max(arr))
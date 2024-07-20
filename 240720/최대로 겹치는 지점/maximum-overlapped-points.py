n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

arr = [0 for _ in range(101)]

for line in lines:
    for i in range(line[0], line[1] + 1):
        arr[i] += 1

print(max(arr))
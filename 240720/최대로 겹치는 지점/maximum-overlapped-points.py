n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

max_x = max(max(lines, key=lambda x : x[1]))
arr = [0 for _ in range(max_x)]

for line in lines:
    for i in range(line[0], line[1]):
        arr[i] += 1

res = 0
for x in arr:
    if x > 1:
        res += 1

print(res)
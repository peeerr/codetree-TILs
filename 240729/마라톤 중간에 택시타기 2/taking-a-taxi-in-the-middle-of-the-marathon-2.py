import sys

n = int(input())
checkpoints = [list(map(int, input().split())) for _ in range(n)]

distance = sys.maxsize 
for i in range(1, n - 1):
    tmp = 0
    for j in range(n - 1):
        if j == i:
            continue
        elif j + 1 == i:
            tmp += abs(checkpoints[j][0] - checkpoints[j + 2][0]) + abs(checkpoints[j][1] - checkpoints[j + 2][1])
        else:
            tmp += abs(checkpoints[j][0] - checkpoints[j + 1][0]) + abs(checkpoints[j][1] - checkpoints[j + 1][1])    
    distance = min(distance, tmp)

print(distance)
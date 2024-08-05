import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_distance = sys.maxsize

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        distance = (((arr[i][0] - arr[j][0]) ** 2) + ((arr[i][1] - arr[j][1]) ** 2)) ** 0.5
        
        if distance < min_distance:
            min_distance = distance

print(round(min_distance ** 2))
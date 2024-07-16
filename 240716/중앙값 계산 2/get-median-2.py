n = int(input())
arr = sorted(map(int, input().split()))

for i in range(len(arr)):
    length = i + 1
    if length % 2 == 1:
        print(arr[0:length][length // 2], end=' ')
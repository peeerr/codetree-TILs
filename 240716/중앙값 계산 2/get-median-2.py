n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    length = i + 1
    if length % 2 == 1:
        print(sorted(arr[:length])[length // 2], end=' ')
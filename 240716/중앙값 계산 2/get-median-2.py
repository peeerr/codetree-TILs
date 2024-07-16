n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if i % 2 == 0:
        print(sorted(arr[:i + 1])[i // 2], end=' ')
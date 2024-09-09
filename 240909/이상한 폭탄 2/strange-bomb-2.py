n, k = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

res = -1

for i in range(n):
    for j in range(i + 1, n):
        if j - i > k:
            continue

        if numbers[i] == numbers[j]:
            res = max(res, numbers[i]) 

print(res)
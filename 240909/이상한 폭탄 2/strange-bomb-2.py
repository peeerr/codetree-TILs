n, k = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

res = []

for i in range(n):
    
    minimum, maximum = i, i
    for _ in range(k):
        if minimum > 0:
            minimum -= 1
        if maximum < n:
            maximum += 1
    
    for j in range(minimum, maximum):
        if i == j:
            continue

        if numbers[i] == numbers[j]:
            res.append(numbers[i])


print(max(res))
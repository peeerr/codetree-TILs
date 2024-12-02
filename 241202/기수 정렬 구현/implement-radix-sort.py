MAX_DIGIT = 6

n = int(input())
arr = list(map(int, input().split()))


for k in range(MAX_DIGIT + 1):
    digit = [[] for _ in range(10)]
    sorted_arr = []

    for x in arr:
        digit[(x // (10 ** k)) % 10].append(x)

    for x in digit:
        sorted_arr.extend(x)

    arr = sorted_arr

print(*arr)

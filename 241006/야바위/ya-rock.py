n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(1, 4):
    score = 0

    for numbers in arr:
        numbers[0], numbers[1] = numbers[1], numbers[0]

        if numbers[numbers[2]] == i:
            score += 1

    ans = max(ans, score)

print(ans)
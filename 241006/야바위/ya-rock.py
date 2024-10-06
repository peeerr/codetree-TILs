n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for start in range(1, 4):
    current_position = start

    score = 0

    for a, b, c in arr:
        if current_position == a:
            current_position = b
        elif current_position == b:
            current_position = a

        if current_position == c:
            score += 1

    ans = max(ans, score)

print(ans)
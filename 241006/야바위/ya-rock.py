n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(1, 4):
    score = 0

    yabawi = [0 for _ in range(4)]
    yabawi[i] = 1

    for a, b, c in arr:
        yabawi[a], yabawi[b] = yabawi[b], yabawi[a]

        if yabawi[c]:
            score += 1

    ans = max(ans, score)

print(ans)
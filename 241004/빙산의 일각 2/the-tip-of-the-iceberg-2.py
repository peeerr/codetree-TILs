n = int(input())
height = [int(input()) for _ in range(n)]

ans = 0

for h in range(1, 1001):
    cnt = 0
    for i in range(n):
        if i == 0 and height[i] - h > 0:
            cnt += 1
        else:
            if height[i - 1] - h <= 0 and height[i] - h > 0:
                cnt += 1
    ans = max(ans, cnt)

print(ans)
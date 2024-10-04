n = int(input())
height = [int(input()) for _ in range(n)]

ans = 0

for h in range(1, 1001):
    cnt = 0

    if height[0] > h:
        cnt += 1

    for i in range(1, n):
        if height[i - 1] <= h and height[i] > h:
            cnt += 1
            
    ans = max(ans, cnt)

print(ans)
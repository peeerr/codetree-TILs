import sys

n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize

for i in range(101):
    for j in range(101):
        
        a1, a2, a3, a4 = 0, 0, 0, 0

        success = True

        for x, y in positions:
            if x == i or y == j:
                success = False
                break

            if x > i and y > j:
                a1 += 1
            elif x < i and y > j:
                a2 += 1
            elif x < i and y < j:
                a3 += 1
            elif x > i and y < j:
                a4 += 1

        if success:
            ans = min(ans, max(a1, a2, a3, a4))

print(ans)
import sys

n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize

for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        
        a1, a2, a3, a4 = 0, 0, 0, 0

        for x, y in positions:

            if x > i and y > j:
                a1 += 1
            elif x < i and y > j:
                a2 += 1
            elif x < i and y < j:
                a3 += 1
            elif x > i and y < j:
                a4 += 1

        ans = min(ans, max(a1, a2, a3, a4))

print(ans)
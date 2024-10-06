n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(11):
    for j in range(i + 1, 11):
        for k in range(j + 1, 11):

            success = True
            
            for pos in positions:
                if pos[0] not in [i, j, k] and pos[1] not in [i, j, k]:
                    success = False
            
            if success:
                ans = 1

print(ans)
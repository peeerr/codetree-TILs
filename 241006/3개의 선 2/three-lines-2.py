n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(11):
    for x_y1 in range(2):
        for j in range(11):
            for x_y2 in range(2):
                for k in range(11):
                    for x_y3 in range(2):

                        success = True
                        
                        for pos in positions:
                            if pos[x_y1] != i and pos[x_y2] != j and pos[x_y3] != k:
                                success = False
                        
                        if success:
                            ans = 1

print(ans)
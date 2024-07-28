import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

coin_num = -sys.maxsize

for i in range(n):
    for j in range(n - 2):
        coin_num = max(coin_num, grid[i][j] + grid[i][j + 1] + grid[i][j + 2])
            
print(coin_num)
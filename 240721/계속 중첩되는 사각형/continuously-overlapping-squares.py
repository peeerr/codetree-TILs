n = int(input())
map(lambda x : int(x) + 100, input().split())

MAX = 200
grid = [['R' for _ in range(MAX)] for _ in range(MAX)]
colour = 'B'

for i in range(2, n + 1):
    if i % 2 == 0:
        colour = 'B'
    else:
        colour = 'R'

    x1, y1, x2, y2 = map(lambda x : int(x) + 100, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = colour

res = 0
for i in range(MAX):
    for j in range(MAX):
        if grid[i][j] == 'B':
            res += 1
print(res)
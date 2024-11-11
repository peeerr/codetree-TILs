def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, m, x, y = map(int, input().split())
directions = input().split()

grid = [[0 for _ in range(n)] for _ in range(n)]
x, y = x - 1, y - 1

grid[x][y] = 6
up, front, right = 1, 2, 3

dxs, dys = {'R': 0, 'L': 0, 'U': -1, 'D': 1}, {'R': 1, 'L': -1, 'U': 0, 'D': 0}

for d in directions:
    nx, ny = x + dxs[d], y + dys[d]

    if not in_range(nx, ny):
        continue 
    
    if d == 'R':
        up, right = 7 - right, up
    elif d == 'L':
        up, right = right, 7 - up
    elif d == 'U':
        up, front = front, 7 - up
    elif d == 'D':
        up, front = 7 - front, up
    
    x, y = nx, ny 
    grid[x][y] = 7 - up

print(sum([sum(x) for x in grid]))
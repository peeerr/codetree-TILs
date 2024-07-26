def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, t = map(int, input().split())
r, c, d = map(lambda x : int(x) if x.isdigit() else x, input().split())

grid = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = {'U': -1, 'D': 1, 'R': 0, 'L': 0}, {'U': 0, 'D': 0, 'R': 1, 'L': -1}

x = r - 1; y = c - 1
for _ in range(t):
    nx, ny = x + dx[d], y + dy[d]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        if d == 'U':
            d = 'D'
        elif d == 'D':
            d = 'U'
        elif d == 'R':
            d = 'L'
        else:
            d = 'R'

print(x + 1, y + 1)
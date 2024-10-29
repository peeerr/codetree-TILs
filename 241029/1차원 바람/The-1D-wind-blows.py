def shift(r, d):
    if d == 'L':
        temp = grid[r][m - 1]
        for i in range(m - 1, 0, - 1):
            grid[r][i] = grid[r][i - 1]
        grid[r][0] = temp
    else:
        temp = grid[r][0]
        for i in range(m - 1):
            grid[r][i] = grid[r][i + 1]
        grid[r][m - 1] = temp


def check_spread(r1, r2):
    for n1, n2 in zip(grid[r1], grid[r2]):
        if n1 == n2:
            return True
    return False


def in_range(r1, r2):
    return 0 <= r1 < n and 0 <= r2 < n


def spread_up(r, d):
    while True:
        if in_range(r, r - 1) and check_spread(r, r - 1):
            d = 'L' if d == 'R' else 'R'
            shift(r - 1, d)
            r = r - 1
        else:
            break


def spread_down(r, d):
    while True:
        if in_range(r, r + 1) and check_spread(r, r + 1):
            d = 'L' if d == 'R' else 'R'
            shift(r + 1, d)
            r = r + 1
        else:
            break


n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
winds = [list(map(lambda x : int(x) - 1 if x.isdigit() else x, input().split())) for _ in range(q)]

for r, d in winds:
    shift(r, d)
    spread_up(r, d)
    spread_down(r, d)

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
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


n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
winds = [list(map(lambda x : int(x) - 1 if x.isdigit() else x, input().split())) for _ in range(q)]

for r, d in winds:
    shift(r, d)
    down_r = r
    down_d = d

    while True:
        is_continue = False
        for i in range(r - 1, -1, -1):
            if check_spread(r, i):
                d = 'L' if d == 'R' else 'R'
                shift(i, d)
                r = i
                is_continue = True
                break
        if not is_continue:
            break

    while True:
        is_continue = False
        for i in range(down_r + 1, n):
            if check_spread(down_r, i):
                down_d = 'L' if down_d == 'R' else 'R'
                shift(i, down_d)
                down_r = i
                is_continue = True
                break
        if not is_continue:
            break

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
def in_range(x, y):
    return 0 <= x <= 4000 and 0 <= y <= 4000


def simulate():
    global marbles, next_marbles, time
    last_collision_time = -1
    dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

    for i, x, y, w, d in marbles:
        nx, ny = x + dxs[d], y + dys[d]

        if not in_range(nx, ny):
            continue
        
        idx = marbles_grid[nx][ny]

        if idx == -1:
            next_marbles.append((i, nx, ny, w, d))
            marbles_grid[nx][ny] = len(next_marbles) - 1
        else:
            last_collision_time = time
            i1, x1, y1, w1, d1 = next_marbles[idx]

            if w > w1 or (w == w1 and i > i1):
                next_marbles[idx] = (i, nx, ny, w, d)

    return last_collision_time


T = int(input())

c = 4000
mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
marbles_grid = [[-1 for _ in range(c + 1)] for _ in range(c + 1)]

for _ in range(T):
    n = int(input())
        
    marbles = []
    time = 1
    ans = -1

    for i in range(1, n + 1):
        x, y, w, d = input().split()
        x, y, w, d = (int(x) + 1000) * 2, (int(y) + 1000) * 2, int(w), mapper[d]
        marbles.append((i, y, x, w, d))

    for _ in range(c + 1):
        next_marbles = []
    
        collision_occur_time = simulate()

        if collision_occur_time != -1:
            ans = collision_occur_time
        time += 1

        for _, x, y, _, _ in next_marbles:
            marbles_grid[x][y] = -1
        marbles = next_marbles[:]

    print(ans)

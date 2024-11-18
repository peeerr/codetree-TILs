from collections import defaultdict


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def combine_duplicate_marbles():
    global marbles
    marbles_dict = defaultdict(list)
    next_marbles = []

    for marble in marbles:
        i, x, y, d, w = marble
        marbles_dict[(x, y)].append([i, x, y, d, w])

    for infos in marbles_dict.values():
        if len(infos) > 1:
            max_i = sorted(infos, key=lambda x : -x[0])[0]
            i, d = max_i[0], max_i[3]
            w = sum([info[4] for info in infos])
            x, y = max_i[1], max_i[2]

            next_marbles.append([i, x, y, d, w])
        else:
            next_marbles.append(infos[0])

    marbles = next_marbles


def move(i, x, y, d, w):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    nx, ny = x + dxs[d], y + dys[d]

    if not in_range(nx, ny):
        return [i, x, y, d ^ 1, w]
    else:
        return [i, nx, ny, d, w]


n, m, t = map(int, input().split())


def move_all():
    global marbles
    next_marbles = []

    for marble in marbles:
        next_marbles.append(move(*marble))
    
    marbles = next_marbles


mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
marbles = []

for i in range(1, m + 1):
    x, y, d, w = input().split()
    x, y, d, w = int(x) - 1, int(y) - 1, mapper[d], int(w)
    marbles.append([i, x, y, d, w])

for _ in range(t):
    move_all()
    combine_duplicate_marbles()

print(len(marbles), max(marbles, key=lambda x : x[4])[4])

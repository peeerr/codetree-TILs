from collections import defaultdict


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move(i, x, y, d, v):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for _ in range(v):
        nx, ny = x + dxs[d], y + dys[d]

        if not in_range(nx, ny):
            d = d ^ 1
            nx, ny = nx + dxs[d] * 2, ny + dys[d] * 2
            
        x, y = nx, ny
    
    return [i, x, y, d, v]


def move_all():
    global marbles
    temp = []

    for info in marbles:
        temp.append(move(*info))

    marbles = temp


def select_marbles():
    global marbles
    marbles_dict = defaultdict(list)
    temp = []

    for info in marbles:
        i, x, y, d, v = info
        marbles_dict[(x, y)].append(info)

    for informations in marbles_dict.values():
        if len(informations) <= k:
            temp.extend(informations)
            continue
        temp.extend(sorted(informations, key=lambda x : (-x[4], -x[0]))[:k])

    marbles = temp


def simulate():
    move_all()
    select_marbles()


mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
n, m, t, k = map(int, input().split())

marbles = []
for i in range(1, m + 1):
    x, y, d, v = input().split()
    x, y, d, v = int(x) - 1, int(y) - 1, mapper[d], int(v)
    marbles.append([i, x, y, d, v])

for _ in range(t):
    simulate()
    
print(len(marbles))

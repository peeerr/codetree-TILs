from collections import defaultdict


def in_range(x, y):
    return -1000 <= x <= 1000 and -1000 <= y <= 1000


def init():
    marbles = []
    mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

    n = int(input())
    for i in range(1, n + 1):
        x, y, w, d = input().split()
        x, y, w, d = int(x), int(y), int(w), mapper[d]
        marbles.append([i, y, x, w, d])

    return marbles


def remove_duplicate_marbles():
    global time, marbles
    marbles_dict = defaultdict(list)
    temp = []
    collision_time = -1
    
    for marble in marbles:
        _, y, x, _, _ = marble
        marbles_dict[(y, x)].append(marble)

    for infos in marbles_dict.values():
        if len(infos) > 1:
            temp.append(sorted(infos, key=lambda k : (-k[3], -k[0]))[0])
            collision_time = time
        else:
            temp.append(infos[0])
    marbles = temp

    return collision_time


def move(i, y, x, w, d):
    global ans, marbles
    dys, dxs = [1, -1, 0, 0], [0, 0, -1, 1]

    ny, nx = y + dys[d], x + dxs[d]

    if not in_range(nx, ny):
        d = d ^ 1
        ny, nx = y + dys[d], x + dxs[d]
    
    for idx, marble in enumerate(marbles):
        if marble[0] == i:
            marbles[idx] = [i, ny, nx, w, d]
            break

    ans = max(ans, remove_duplicate_marbles())


def move_all():
    for marble in marbles:
        move(*marble)


def simulate():
    global ans, time

    for _ in range(2000):
        move_all()
        time += 2

    print(ans)


T = int(input())

for asd in range(T):
    ans, time = -1, 2

    marbles = init()
    simulate()

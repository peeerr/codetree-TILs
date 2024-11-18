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
        marbles.append([i, y, x, w, d, False])

    return marbles


def remove_duplicate_marbles():
    global time, marbles
    marbles_dict = defaultdict(list)
    temp = []
    collision_time = -1
    
    for marble in marbles:
        _, y, x, _, _, _ = marble
        marbles_dict[(y, x)].append(marble)

    for infos in marbles_dict.values():
        if len(infos) > 1:
            if ((infos[0][5] and not infos[1][5]) or (not infos[0][5] and infos[1][5])) and infos[1][4] ^ 1 == infos[0][4]:
                collision_time = time - 1
                temp.append(sorted(infos, key=lambda k : (-k[3], -k[0]))[0])
            elif infos[0][5] and infos[1][5]:
                collision_time = time
                temp.append(sorted(infos, key=lambda k : (-k[3], -k[0]))[0])
            else:
                temp.extend(infos)
        else:
            temp.append(infos[0])
    marbles = temp

    return collision_time


def move(i, y, x, w, d, moved):
    global ans, marbles
    dys, dxs = [1, -1, 0, 0], [0, 0, -1, 1]

    ny, nx = y + dys[d], x + dxs[d]

    if not in_range(nx, ny):
        return
    
    for idx, marble in enumerate(marbles):
        if marble[0] == i:
            marbles[idx] = [i, ny, nx, w, d, not moved]
            break

    ans = max(ans, remove_duplicate_marbles())


def move_all():
    for marble in marbles:
        move(*marble)
    for idx in range(len(marbles)):
        marbles[idx][5] = False


def simulate():
    global ans, time

    for _ in range(2000):
        move_all()
        time += 2

    print(ans)


T = int(input())

for _ in range(T):
    ans, time = -1, 2

    marbles = init()
    simulate()

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
            i1, x1, y1, w1, d1, moved1 = infos[0]
            i2, x2, y2, w2, d2, moved2 = infos[1]
            if ((moved1 and not moved2) or (not moved1 and moved2)) and d1 ^ 1 == d2:
                collision_time = time - 1
                if w1 > w2:
                    temp.append([i1, x1, y1, w1, d1, moved1])
                elif w1 < w2:
                    temp.append([i2, x2, y2, w2, d2, moved2])
                else:
                    if i1 > i2:
                        temp.append([i1, x1, y1, w1, d1, moved1])
                    else:
                        temp.append([i2, x2, y2, w2, d2, moved2])
            elif moved1 and moved2:
                collision_time = time
                if w1 > w2:
                    temp.append([i1, x1, y1, w1, d1, moved1])
                elif w1 < w2:
                    temp.append([i2, x2, y2, w2, d2, moved2])
                else:
                    if i1 > i2:
                        temp.append([i1, x1, y1, w1, d1, moved1])
                    else:
                        temp.append([i2, x2, y2, w2, d2, moved2])
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

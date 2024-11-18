from collections import defaultdict

def in_range(x, y):
    return -2000 <= x <= 2000 and -2000 <= y <= 2000

def init():
    marbles = [None] * 101  # N의 최대값이 100이므로
    mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

    n = int(input())
    for i in range(1, n + 1):
        x, y, w, d = input().split()
        x, y, w, d = int(x) * 2, int(y) * 2, int(w), mapper[d]
        marbles[i] = [y, x, w, d]  # ID를 인덱스로 사용

    return marbles, n

def remove_duplicate_marbles():
    global time, marbles, n
    marbles_dict = defaultdict(list)
    collision_time = -1
    
    # 존재하는 구슬만 처리
    for i in range(1, n + 1):
        if marbles[i]:
            y, x, w, d = marbles[i]
            marbles_dict[(y, x)].append((i, y, x, w, d))

    # 충돌 처리
    for infos in marbles_dict.values():
        if len(infos) > 1:
            # 가장 무거운/번호가 큰 구슬 찾기
            winner = max(infos, key=lambda x: (x[3], x[0]))
            # 나머지 구슬 제거
            for i, *_ in infos:
                if i != winner[0]:
                    marbles[i] = None
            collision_time = time
            # 승자 구슬 위치 업데이트
            marbles[winner[0]] = list(winner[1:])
        else:
            i, y, x, w, d = infos[0]
            marbles[i] = [y, x, w, d]

    return collision_time

def move_all():
    global ans, n
    dys, dxs = [1, -1, 0, 0], [0, 0, -1, 1]

    # 한 번에 모든 구슬 이동
    for i in range(1, n + 1):
        if marbles[i]:
            y, x, w, d = marbles[i]
            ny, nx = y + dys[d], x + dxs[d]
            if in_range(nx, ny):
                marbles[i] = [ny, nx, w, d]
            else:
                marbles[i] = None

    collision_time = remove_duplicate_marbles()
    if collision_time != -1:
        ans = collision_time

def simulate():
    global ans, time

    for _ in range(4000):
        if sum(1 for m in marbles[1 : n + 1] if m) <= 1:  # 구슬이 1개 이하면 종료
            break
        move_all()
        time += 1

    print(ans)

T = int(input())

for _ in range(T):
    ans, time = -1, 1
    marbles, n = init()
    simulate()

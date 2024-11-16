def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    
    mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    count = [[0 for _ in range(n)] for _ in range(n)]
    marbles = set()
    
    # 구슬 정보 초기화
    for _ in range(m):
        x, y, d = input().split()
        marbles.add((int(x) - 1, int(y) - 1, mapper[d]))
    for x, y, _ in marbles:
        count[x][y] = 1

    for _ in range(n * 2):
        # 구슬 이동 및 이동된 위치 저장
        temp = set()
        for x, y, d in marbles:
            nx, ny = x + dxs[d], y + dys[d]

            if not in_range(nx, ny):
                temp.add((x, y, d ^ 1))
                continue
            
            temp.add((nx, ny, d))
            count[x][y] -= 1
            count[nx][ny] += 1

        # 충돌한 구슬 제거
        marbles = set()
        for x, y, d in temp:
            if count[x][y] > 1:
                count[x][y] = 0
            elif count[x][y] == 1:
                marbles.add((x, y, d))

    print(len(marbles))

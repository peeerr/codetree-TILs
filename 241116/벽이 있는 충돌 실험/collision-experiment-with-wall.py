def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


T = int(input())
count = [[0 for _ in range(50)] for _ in range(50)]

for _ in range(T):
    n, m = map(int, input().split())
    
    mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    marbles = []
    
    # 구슬 정보 초기화
    for _ in range(m):
        x, y, d = input().split()
        marbles.append((int(x) - 1, int(y) - 1, mapper[d]))
    for x, y, _ in marbles:
        count[x][y] = 1

    for _ in range(n * 2):
        # 구슬 이동 및 이동된 위치 저장
        for i, (x, y, d) in enumerate(marbles):
            nx, ny = x + dxs[d], y + dys[d]

            if not in_range(nx, ny):
                marbles[i] = (x, y, d ^ 1)
                continue
            
            marbles[i] = (nx, ny, d)
            count[x][y] -= 1
            count[nx][ny] += 1

        # 충돌한 구슬 제거
        temp = []
        for x, y, d in marbles:
            if count[x][y] > 1:
                count[x][y] = 0
            elif count[x][y] == 1:
                temp.append((x, y, d))

        marbles = temp

    print(len(marbles))

    # 한 테스트케이스 끝나면 남은 모든 구슬 제거
    for x, y, _ in marbles:
        count[x][y] = 0

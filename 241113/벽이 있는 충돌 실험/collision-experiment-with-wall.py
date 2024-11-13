def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    infos = [tuple(map(lambda x : int(x) - 1 if x.isdigit() else x, input().split())) for _ in range(m)]

    grid = [[0 for _ in range(n)] for _ in range(n)]
    mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    
    for i, (x, y, d) in enumerate(infos):
        infos[i] = [x, y, mapper[d]]

    for x, y, _ in infos:
        grid[x][y] = 1
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for _ in range(n * 2):
        for i, (x, y, d) in enumerate(infos):
            nx, ny = x + dxs[d], y + dys[d]

            if not in_range(nx, ny):
                infos[i] = [x, y, d ^ 1]
                continue
            
            infos[i] = [nx, ny, d]
            grid[nx][ny] += 1
            grid[x][y] -= 1

        # 충돌한 구슬 제거
        positions = {}

        # 각 구슬의 현재 위치를 기록
        for i, (x, y, d) in enumerate(infos):
            if (x, y) not in positions:
                positions[(x, y)] = []
            positions[(x, y)].append(i)

        remove_indices = set()
        # 충돌이 발생한 위치만 확인
        for pos, indices in positions.items():
            if len(indices) > 1:  # 한 위치에 2개 이상의 구슬이 있는 경우
                x, y = pos
                grid[x][y] = 0
                for idx in indices:
                    remove_indices.add(idx)

        # 인덱스가 큰 것부터 제거 (작은 인덱스부터 제거하면 나머지 인덱스가 변경됨)
        for idx in sorted(remove_indices, reverse=True):
            infos.pop(idx)

    print(sum([1 if grid[x][y] == 1 else 0 for y in range(n) for x in range(n)]))

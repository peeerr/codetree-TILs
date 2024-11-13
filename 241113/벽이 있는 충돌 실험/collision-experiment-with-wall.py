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
        remove_data = []

        for x in range(n):
            for y in range(n):
                if grid[x][y] > 1:
                    for nx, ny, d in infos:
                        if x == nx and y == ny:
                            remove_data.append([nx, ny, d])
                    grid[x][y] = 0
        
        for data in remove_data:
            infos.remove(data)

    print(sum([1 if grid[x][y] == 1 else 0 for y in range(n) for x in range(n)]))

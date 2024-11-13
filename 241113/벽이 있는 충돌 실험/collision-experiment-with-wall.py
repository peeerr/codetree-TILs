def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    infos = [tuple(map(lambda x: int(x) - 1 if x.isdigit() else x, input().split())) for _ in range(m)]
    
    # 방향 매핑
    mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # 초기 구슬 정보 변환
    marbles = []  # [x, y, direction] 형태로 저장
    for x, y, d in infos:
        marbles.append([x, y, mapper[d]])
    
    # 2n번 이동
    for _ in range(n * 2):
        # 1. 모든 구슬 이동
        for i, (x, y, d) in enumerate(marbles):
            nx, ny = x + dxs[d], y + dys[d]
            
            # 벽에 부딪히면 방향 전환
            if not in_range(nx, ny):
                marbles[i][2] = d ^ 1
                continue
            
            # 위치 업데이트
            marbles[i][0], marbles[i][1] = nx, ny
        
        # 2. 충돌 체크
        positions = {}
        remove_set = set()
        
        for i, (x, y, d) in enumerate(marbles):
            pos = (x, y)
            if pos not in positions:
                positions[pos] = []
            positions[pos].append(i)
            
            # 충돌 발생
            if len(positions[pos]) > 1:
                remove_set.update(positions[pos])
        
        # 3. 충돌한 구슬 제거 (인덱스가 큰 것부터)
        for idx in sorted(remove_set, reverse=True):
            marbles.pop(idx)
    
    print(len(marbles))

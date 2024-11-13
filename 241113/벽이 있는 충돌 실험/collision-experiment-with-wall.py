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
        # 1. 구슬 이동
        new_positions = {}  # (x, y) -> 해당 위치의 구슬 인덱스들
        remove_set = set()  # 제거할 구슬 인덱스
        
        for i, (x, y, d) in enumerate(marbles):
            if i in remove_set:  # 이미 제거 예정인 구슬은 건너뜀
                continue
                
            # 다음 위치 계산
            nx, ny = x + dxs[d], y + dys[d]
            
            # 벽에 부딪히면 방향 전환
            if not in_range(nx, ny):
                marbles[i][2] = d ^ 1  # 방향 반전
                continue
            
            # 위치 업데이트
            marbles[i][0], marbles[i][1] = nx, ny
            
            # 새 위치에 구슬 기록
            pos = (nx, ny)
            if pos not in new_positions:
                new_positions[pos] = []
            new_positions[pos].append(i)
            
            # 충돌 체크
            if len(new_positions[pos]) > 1:
                remove_set.update(new_positions[pos])
        
        # 충돌한 구슬 제거 (인덱스가 큰 것부터)
        for idx in sorted(remove_set, reverse=True):
            marbles.pop(idx)
    
    print(len(marbles))
    
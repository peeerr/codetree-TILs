import sys


def calc(infos):
    # 높이(h) 순으로 정렬
    infos.sort(key=lambda x: x[1])
    result = [i for i in range(n + 1)]  # 초기 위치 설정
    
    # 각 가로선마다
    for w, h in infos:
        # w 위치와 w+1 위치를 교환
        result[w], result[w + 1] = result[w + 1], result[w]
    
    return result[1:]


def f(h, idx):
    global ans

    if len(selected) == m:
        return

    for w in range(idx, n):
        if len(selected) > 0 and selected[-1][0] == w - 1 and selected[-1][1] == h:
            continue
            
        selected.append((w, h))
        
        res = calc(selected)
        if res == result:
            ans = min(ans, len(selected))
            
        f(h, w + 1)
        selected.pop()
    
    if h < 6:
        f(h + 1, 1)


n, m = map(int, input().split())
infos = [tuple(map(int, input().split())) for _ in range(m)]
selected = []

initial = [i for i in range(1, n + 1)]
if calc(infos) == initial:
    print(0)
    exit()

result = calc(infos)
ans = sys.maxsize
f(1, 1)

print(ans)

N, K, P, T = map(int, input().split())

handshake_cnt = [K for _ in range(101)]
infectee = [False for _ in range(101)]
infectee[P] = True

handshakes = sorted([list(map(int, input().split())) for _ in range(T)], key=lambda x : x[0])

for handshake in handshakes:
    t, x, y = handshake

    if (not infectee[x] and infectee[y]) and handshake_cnt[y] > 0:
        infectee[x] = True
        handshake_cnt[y] -= 1
    elif (infectee[x] and not infectee[y]) and handshake_cnt[x] > 0 :
        infectee[y] = True
        handshake_cnt[x] -= 1
    elif (infectee[x] and infectee[y]) and (handshake_cnt[x] > 0 or handshake_cnt[y] > 0):
        handshake_cnt[x] -= 1
        handshake_cnt[y] -= 1

for i in range(1, N + 1):
    if infectee[i]:
        print(1, end='')
    else:
        print(0, end='')
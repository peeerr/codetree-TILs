N, K, P, T = map(int, input().split())

arr = [0 for _ in range(251)]
infectee = [False for _ in range(101)]
infectee[P] = True

handshakes = sorted([list(map(int, input().split())) for _ in range(T)], key=lambda x : x[0])

for handshake in handshakes:
    t, x, y = handshake

    if (not infectee[x] and infectee[y]) and K != 0:
        arr[t] = x
        infectee[x] = True
        K -= 1
    elif infectee[x] and not infectee[y] and K != 0:
        arr[t] = y
        infectee[y] = True
        K -= 1
    elif infectee[x] and infectee[y]:
        K -= 1

for i in range(1, N + 1):
    if infectee[i]:
        print(1, end='')
    else:
        print(0, end='')
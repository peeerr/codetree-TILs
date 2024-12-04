import sys

MAX_INT = sys.maxsize


n, m = map(int, input().split())
coins = list(map(int, input().split()))

d = [0 for i in range(m + 1)]

for i in range(1, m + 1):
    min_cnt = MAX_INT
    for coin in coins:
        if i - coin >= 0:
            min_cnt = min(min_cnt, d[i - coin])
    d[i] = min_cnt + 1

print(-1 if d[m] == MAX_INT + 1 else d[m])

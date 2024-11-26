import sys
from collections import deque


def bfs():
    ans = sys.maxsize

    while q:
        n, cnt = q.popleft()

        if n == 1:
            ans = min(ans, cnt)
        elif n % 3 == 0 and n % 2 == 0:
            q.append((n / 3, cnt + 1))
            q.append((n / 2, cnt + 1))
        elif n % 3 == 0:
            q.append((n / 3, cnt + 1))
        elif n % 2 == 0:
            q.append((n / 2, cnt + 1))
        else:
            q.append((n + 1, cnt + 1))
            q.append((n - 1, cnt + 1))
    
    return ans


n = int(input())
q = deque([(n, 0)])

print(bfs())

import sys
from collections import deque


def bfs():
    visited = set()

    while q:
        n, cnt = q.popleft()

        if n == 1:
            return cnt
        
        lst = [n + 1, n - 1]
        if n % 2 == 0:
            lst.append(n // 2)
        if n % 3 == 0:
            lst.append(n // 3)
        
        for x in lst:
            if x not in visited:
                q.append((x, cnt + 1))
                visited.add(x)


n = int(input())
q = deque([(n, 0)])

print(bfs())

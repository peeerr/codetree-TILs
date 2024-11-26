import sys
from collections import deque


def bfs():
    visited = set()

    while q:
        n, cnt = q.popleft()

        if n == 1:
            return cnt
        elif n % 2 == 0 and n % 3 == 0:
            if n + 1 not in visited:
                q.append((n + 1, cnt + 1))
                visited.add(n + 1)
            if n - 1 not in visited:
                q.append((n - 1, cnt + 1))
                visited.add(n - 1)
            if n // 2 not in visited:
                q.append((n // 2, cnt + 1))
                visited.add(n // 2)
            if n // 3 not in visited:
                q.append((n // 3, cnt + 1))
                visited.add(n // 3)
        elif n % 2 == 0:
            if n + 1 not in visited:
                q.append((n + 1, cnt + 1))
                visited.add(n + 1)
            if n - 1 not in visited:
                q.append((n - 1, cnt + 1))
                visited.add(n - 1)
            if n // 2 not in visited:
                q.append((n // 2, cnt + 1))
                visited.add(n // 2)
        elif n % 3 == 0:
            if n + 1 not in visited:
                q.append((n + 1, cnt + 1))
                visited.add(n + 1)
            if n - 1 not in visited:
                q.append((n - 1, cnt + 1))
                visited.add(n - 1)
            if n // 3 not in visited:
                q.append((n // 3, cnt + 1))
                visited.add(n // 3)
        else:
            if n + 1 not in visited:
                q.append((n + 1, cnt + 1))
                visited.add(n + 1)
            if n - 1 not in visited:
                q.append((n - 1, cnt + 1))
                visited.add(n - 1)
    
    return ans


n = int(input())
q = deque([(n, 0)])

print(bfs())

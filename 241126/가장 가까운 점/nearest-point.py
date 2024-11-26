import heapq

n, m = map(int, input().split())
pq = []

for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(pq, (abs(x) + abs(y), x, y))

for _ in range(m):
    _, x, y = heapq.heappop(pq)
    x, y = x + 2, y + 2
    heapq.heappush(pq, (abs(x) + abs(y), x, y))

print(pq[0][1], pq[0][2])

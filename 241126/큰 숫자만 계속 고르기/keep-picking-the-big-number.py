import heapq

n, m = map(int, input().split())
nums = list(map(int, input().split()))

pq = []
for num in nums:
    heapq.heappush(pq, -num)

for _ in range(m):
    n = -heapq.heappop(pq)
    heapq.heappush(pq, -(n - 1))

print(-pq[0])

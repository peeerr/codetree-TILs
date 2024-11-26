import heapq


n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]

pq = []
ans = 0
last = 0

for start, end in meeting:
    heapq.heappush(pq, (end, start))

while pq:
    end, start = heapq.heappop(pq)

    if last <= start:
        ans += 1
        last = end

print(ans)

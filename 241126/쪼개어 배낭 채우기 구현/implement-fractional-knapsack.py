import heapq


n, m = map(int, input().split())
pq = []

for _ in range(n):
    w, v = map(int, input().split())
    heapq.heappush(pq, (-(v / w), w, v))

weight = 0
ans = 0.0

while weight != m:
    _, w, v = heapq.heappop(pq)

    weight += w
    ans += v

    if weight > m:
        weight -= w
        ans -= v
        
        split_jewel = (m - weight) / w

        weight += w * split_jewel
        ans += v * split_jewel

print(f"{ans:.3f}")

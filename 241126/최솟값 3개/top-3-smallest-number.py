import heapq

n = int(input())
nums = list(map(int, input().split()))

pq = []

for num in nums:
    heapq.heappush(pq, num)

    if len(pq) < 3:
        print(-1)
    else:
        n1 = heapq.heappop(pq)
        n2 = heapq.heappop(pq)
        n3 = heapq.heappop(pq)
        print(n1 * n2 * n3)
        heapq.heappush(pq, n1)
        heapq.heappush(pq, n2)
        heapq.heappush(pq, n3)

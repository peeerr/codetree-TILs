import heapq

n = int(input())
nums = list(map(int, input().split()))

pq = []

for num in nums:
    heapq.heappush(pq, num)

    if len(pq) < 3:
        print(-1)
    else:
        print(pq[0] * pq[1] * pq[2])

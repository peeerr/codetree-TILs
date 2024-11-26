import heapq


n = int(input())
nums = list(map(int, input().split()))

pq = []

for num in nums:
    heapq.heappush(pq, num)

ans = 0

while len(pq) != 1:
    num1 = heapq.heappop(pq)
    num2 = heapq.heappop(pq)

    heapq.heappush(pq, num1 + num2)
    ans += num1 + num2

print(ans)

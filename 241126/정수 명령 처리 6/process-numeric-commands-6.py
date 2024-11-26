import heapq

class PriorityQuere:
    def __init__(self):
        self.items = []

    def push(self, a):
        heapq.heappush(self.items, -a)

    def pop(self):
        print(-heapq.heappop(self.items))

    def size(self):
        print(len(self.items))

    def empty(self):
        print(1 if not self.items else 0)

    def top(self):
        print(-self.items[0])


pq = PriorityQuere()
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        pq.push(int(command[1]))
    else:
        eval("pq." + command[0] + "()")

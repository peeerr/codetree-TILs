n = int(input())

x, y = 0, 0

dx, dy = {'W': -1, 'S': 0, 'N': 0, 'E': 1}, {'W': 0, 'S': -1, 'N': 1, 'E': 0}

for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)

    x, y = x + dx[direction] * distance, y + dy[direction] * distance

print(x, y)
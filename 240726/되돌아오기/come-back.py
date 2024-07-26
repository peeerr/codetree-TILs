n = int(input())

dx, dy = {'N': 1, 'S': -1, 'E': 0, 'W': 0}, {'N': 0, 'S': 0, 'E': 1, 'W': -1}
x, y = 0, 0
ans = 0
success = 0

for _ in range(n):
    direction, distance = input().split()

    for _ in range(int(distance)):
        nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny
        ans += 1
        
        if x == 0 and y == 0:
            success = 1
            break
        
    if success == 1:
        break

print(ans if success == 1 else -1)
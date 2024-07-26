inst = list(input())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0 
direction = 0
for d in inst:
    if d == 'L':
        direction = (direction + 3) % 4
    elif d == 'R':
        direction = (direction + 1) % 4
    else:
        x, y = x + dx[direction], y + dy[direction]

print(x, y)
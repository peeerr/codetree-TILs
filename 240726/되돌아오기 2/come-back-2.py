inst = list(input())

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

x, y = 0, 0
direction = 0
success = 0
ans = 0

for i in inst:
    if i == 'F':
        x, y = x + dx[direction], y + dy[direction]
        ans += 1

        if x == 0 and y == 0:
            success = 1
            break

    elif i == 'R':
        direction = (direction + 1) % 4
        ans += 1
    else:
        direction = (direction - 1 + 4) % 4
        ans += 1

print(ans if success == 1 else -1)
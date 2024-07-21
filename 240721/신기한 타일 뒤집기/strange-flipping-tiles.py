n = int(input())

grid = ['' for _ in range(200001)]

start_pos = 100000
direction = 0
colour = ''
for _ in range(n):
    instruction = input().split()
    instruction[0] = int(instruction[0])

    if instruction[1] == 'L':
        direction = -1
        colour = 'W'
    else:
        direction = 1
        colour = 'B'

    for i in range(start_pos, start_pos + (instruction[0] * direction), direction):
        grid[i] = colour
        start_pos = i

print(len([x for x in grid if x == 'W']), end=' ')
print(len([x for x in grid if x == 'B']))
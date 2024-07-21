n = int(input())

grid = [['', 0] for _ in range(200001)]

start_pos = 100000
color = ''
direction = 0
for _ in range(n):
    instructions = input().split()
    instructions[0] = int(instructions[0])

    if instructions[1] == 'L':
        color = 'W'
        direction = -1
    else:
        color = 'B'
        direction = 1

    for i in range(start_pos, (start_pos + (instructions[0] * direction)), direction):
        if grid[i][0] != color and grid[i][0] != 'G':
            grid[i][1] += 1
            grid[i][0] = color

        if grid[i][1] == 4:
            grid[i][1] = -1
            grid[i][0] = 'G'

        start_pos = i


print(len([x for x in grid if x[0] == 'W']), end=' ')
print(len([x for x in grid if x[0] == 'B']), end=' ')
print(len([x for x in grid if x[0] == 'G']), end=' ')
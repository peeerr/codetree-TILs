n = int(input())

grid = [['', [0, 0]] for _ in range(200001)]

start_pos = 100000
colour = ''
direction = 0
for _ in range(n):
    instructions = input().split()
    instructions[0] = int(instructions[0])

    if instructions[1] == 'L':
        colour = 'W'
        direction = -1
    else:
        colour = 'B'
        direction = 1

    for i in range(start_pos, (start_pos + (instructions[0] * direction)), direction):
        if grid[i][0] != colour and grid[i][0] != 'G':
            grid[i][0] = colour

        if colour == 'W':
            grid[i][1][0] += 1
        else:
            grid[i][1][1] += 1

        if grid[i][1][0] >= 2 and grid[i][1][1] >= 2:
            grid[i][1][0] = float('-inf')
            grid[i][0] = 'G'

        start_pos = i


print(len([x for x in grid if x[0] == 'W']), end=' ')
print(len([x for x in grid if x[0] == 'B']), end=' ')
print(len([x for x in grid if x[0] == 'G']), end=' ')
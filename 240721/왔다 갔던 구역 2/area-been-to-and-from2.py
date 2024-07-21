n = int(input())
instructions = [list(map(lambda x : int(x) if x.isdigit() else x , input().split())) for _ in range(n)]

grid = [0 for _ in range(2001)]

start_pos = 1000
direction = 0
end_pos = 0
last_dir = 'K'
for inst in instructions:
    if inst[1] == 'R':
        direction = 1
    else:
        direction = -1
    if inst[1] == last_dir:
        start_pos += (1 * direction)
    last_dir = inst[1]
    for i in range(start_pos, (start_pos + (inst[0] * direction)), direction):
        grid[i] += 1
        start_pos = i

print(len([x for x in grid if x >= 2]))
n = int(input())
positions = sorted([list(map(int, input().split())) + [i] for i in range(1, n + 1)], key=lambda x : (abs(x[0]) + abs(x[1]), x[2]))

for pos in positions:
    print(pos[2])
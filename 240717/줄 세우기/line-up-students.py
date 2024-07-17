n = int(input())
hw = sorted([list(map(int, input().split())) + [i] for i in range(1, n + 1)], key=lambda x : (-x[0], -x[1], x[2]))

for x in hw:
    print(x[0], x[1], x[2])
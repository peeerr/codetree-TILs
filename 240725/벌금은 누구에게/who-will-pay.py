n, m, k = map(int, input().split())
targets = [int(input()) for _ in range(m)]

students = [0 for _ in range(n + 1)]

for target in targets:
    students[target] += 1

    if students[target] == k:
        print(target)
        break
n = int(input())
arr = sorted([input().split() + [str(i)] for i in range(1, n + 1)], key=lambda x : (int(x[0]), -int(x[1])))

for x in arr:
    print(" ".join(x))
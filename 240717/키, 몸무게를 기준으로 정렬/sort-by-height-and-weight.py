n = int(input())
arr = sorted([input().split() for _ in range(n)], key=lambda x : (int(x[1]), -(int(x[2]))))

for x in arr:
    print(" ".join(x))
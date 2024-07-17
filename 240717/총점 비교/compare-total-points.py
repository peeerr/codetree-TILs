n = int(input())
arr = sorted([input().split() for _ in range(n)], key=lambda x : int(x[1]) + int(x[2]) + int(x[3]))

for x in arr:
    print(f"{' '.join(x)}")
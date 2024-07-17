n = int(input())
arr = sorted([input().split() for _ in range(n)], key=lambda x : x[1])

for x in arr:
    print(f"{' '.join(x)}")
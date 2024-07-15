n = int(input())
arr = list(map(int, input().split()))

for x in sorted(arr):
    print(x, end=' ')
print()
for x in sorted(arr, reverse=True):
    print(x, end=' ')
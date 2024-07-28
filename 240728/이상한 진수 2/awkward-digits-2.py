import sys

a = list(map(int, list(input())))
max_n = -sys.maxsize

for i in range(len(a)):
    a[i] = 1 - a[i]
    
    n = 0
    for x in a:
        n = n * 2 + x

    max_n = max(n, max_n)
    a[i] = 1 - a[i]

print(max_n)
import sys

def binary_to_decimal():
    n = 0
    for i, x in enumerate(reversed(a)):
        n += x * (2 ** i)
    return n


a = list(map(int, list(input())))
max_n = -sys.maxsize

for i in range(len(a)):
    a[i] = abs(a[i] - 1)
    max_n = max(max_n, binary_to_decimal())
    a[i] = abs(a[i] - 1)

print(max_n)
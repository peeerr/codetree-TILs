def s(n):
    if n == 1:
        return 1
    return s(n - 1) + n

n = int(input())
print(s(n))
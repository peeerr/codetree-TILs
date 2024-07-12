def p(n):
    if n == 0:
        return
    p(n - 1)
    print(n, end=' ')

def r(n):
    if n == 0:
        return
    print(n, end=' ')
    r(n - 1)

n = int(input())
p(n)
print()
r(n)
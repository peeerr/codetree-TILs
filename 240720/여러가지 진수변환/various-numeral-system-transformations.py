n, b = map(int, input().split())

res = ''
while n != 1:
    res += str(n % b)
    n //= b
    if n == 1:
        res += str(1)

print(res[::-1])
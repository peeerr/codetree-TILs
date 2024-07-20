n, b = map(int, input().split())

res = ''
while True:
    res += str(n % b)
    n //= b
    if n == 1:
        res += str(1)
        break
    elif n == 0:
        break

print(res[::-1])
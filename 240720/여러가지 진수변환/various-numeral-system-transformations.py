n, b = map(int, input().split())

res = ''
while True:
    if n < b:
        res += str(n)
        break
    res += str(n % b)
    n //= b

print(res[::-1])
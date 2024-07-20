n = int(input())

res = ''
while n != 0:
    res += str(n % 2)
    n //= 2

print(res[::-1])
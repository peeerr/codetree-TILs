def a_to_digit(a, n):
    res = 0
    for x in n:
        res = res * a + x
    return res


def digit_to_b(b, n):
    res = ''
    while True:
        if n < b:
            res += str(n)
            break
        res += str(n % b)
        n //= b
    return res[::-1]


a, b = map(int, input().split())
n = list(map(int, list(input())))

n = a_to_digit(a, n)
res = digit_to_b(b, n)

print(res)
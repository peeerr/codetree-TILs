def binary_to_digit(b):
    res = 0
    for x in b:
        res = res * 2 + x
    return res


def digit_to_binary(n):
    res = ''
    while True:
        if n < 2:
            res += str(n)
            break
        res += str(n % 2)
        n //= 2
    return int(res[::-1])


binary = list(map(int, list(input())))

d = binary_to_digit(binary) * 17
b = digit_to_binary(d)

print(b)
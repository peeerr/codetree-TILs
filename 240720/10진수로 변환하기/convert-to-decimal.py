n = list(map(int, list(input())))

res = 0
for cnt, x in enumerate(n[::-1]):
    res += x * (2 ** cnt)

print(res)
n = list(map(int, list(input())))

res = 0
for x in n:
    res = res * 2 + x

print(res)
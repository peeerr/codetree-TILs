x, y = map(int, input().split())

ans = 0

for n in range(x, y + 1):
    correct = True
    
    num = str(n)
    length = len(num)

    for i in range(length // 2 + 1):
        if num[i] != num[length - i - 1]:
            correct = False
    
    if correct:
        ans += 1

print(ans)
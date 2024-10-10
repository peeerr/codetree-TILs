n = int(input())
s = input()

ans = 0

for i in range(1, n):
    cnt = 0
    dupl = []
    success = True

    for j in range(n - i + 1):
        tmp = s[j : j + i]
        
        if tmp in dupl:
            success = False
            break
        dupl.append(tmp)

    if success:
        ans = i
        break

print(ans)
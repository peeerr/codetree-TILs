s = list(input())

ans = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == '(' and s[j] == ')':
            ans += 1

print(ans)
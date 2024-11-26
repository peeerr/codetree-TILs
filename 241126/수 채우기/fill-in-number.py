import sys


n = int(input())

if n == 1:
    print(-1)
    sys.exit()

ans = 0

while n > 0:
    n -= 5
    ans += 1

    if n == -1 or n == 1:
        n += 5
        ans -= 1
        while n != 0:
            n -= 2
            ans += 1

print(ans)

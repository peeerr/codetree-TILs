import sys


n = int(input())
arr = list(map(int, input().split()))

ans = 0
temp = -sys.maxsize

for x in arr:    
    if temp < 0:
        temp = x
    else:
        temp += x

    ans = max(ans, temp)

print(ans)

import sys


n = int(input())
arr = list(map(int, input().split()))

ans = -sys.maxsize
temp = 0

for x in arr:    
    if temp < 0:
        temp = x
    else:
        temp += x

    ans = max(ans, temp)

print(ans)

n = int(input())
arr = list(map(int, input().split()))

ans = 0
temp = 0

if max(arr) <= 0:
    print(max(arr))
else:
    for x in arr:
        temp += x
        
        if temp > 0:
            ans = max(ans, temp)
        else:
            temp = 0

    print(ans)

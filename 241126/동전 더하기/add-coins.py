n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

num = 0
ans = 0

for coin in coins[::-1]:
    if num == k:
        break
    
    while k - num >= coin:
        ans += 1
        num += coin
        
print(ans)

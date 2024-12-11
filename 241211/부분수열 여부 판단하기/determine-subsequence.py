n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt, j = 0, 0

for i in range(m):
    while j < n and a[j] != b[i]:
        j += 1
    
    if j >= n:
        break

    cnt += 1
    
print('Yes' if cnt == m else 'No')

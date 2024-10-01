n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):

            tmp = [0 for _ in range(101)]

            for l in range(n):
                if l == i or l == j or l == k:
                    continue

                for x in range(arr[l][0], arr[l][1] + 1):
                    tmp[x] += 1

            success = True
            for x in tmp:
                if x >= 2:
                    success = False
                    break
            
            if success:
                ans += 1

print(ans)
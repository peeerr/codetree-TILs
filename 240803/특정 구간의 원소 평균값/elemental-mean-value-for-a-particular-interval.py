n = int(input())
arr = list(map(int, input().split()))

res = 0

for k in range(1, n + 1):
    for i in range(n - k + 1):
        interval_sum = sum(arr[i:i + k])
        if interval_sum / k in arr[i:i + k]:
            res += 1

print(res)
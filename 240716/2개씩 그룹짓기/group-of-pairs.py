n = int(input())
arr = sorted(list(map(int, input().split())))

res = [0 for _ in range(n)]
i = 0

while arr:
    i %= n
    res[i] += arr.pop(0) + arr.pop(-1)
    i += 1

print(max(res))
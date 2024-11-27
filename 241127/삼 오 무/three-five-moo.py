def calc(num):
    return num - (num // 3 + num // 5 - num // 15)


n = int(input())

ans = 10 ** 9
left, right = 1, 10 ** 9

while left <= right:
    mid = (left + right) // 2
    idx = calc(mid)

    if idx >= n:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)

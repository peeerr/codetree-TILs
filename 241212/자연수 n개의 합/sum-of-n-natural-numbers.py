def search(s):
    left, right = 0, s
    max_n = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 <= s:
            max_n = max(max_n, mid)
            left = mid + 1
        else:
            right = mid - 1

    return max_n


s = int(input())
print(search(s))

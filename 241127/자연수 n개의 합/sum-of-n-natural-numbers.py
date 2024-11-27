def binary_search():
    left, right = 1, s
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 <= s:
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

    return ans


s = int(input())
print(binary_search())
